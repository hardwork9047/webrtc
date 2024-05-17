const localVideo = document.getElementById('localVideo');
const remoteVideo = document.getElementById('remoteVideo');
const socket = io();

// WebRTCの初期化
const configuration = {'iceServers': [{'urls': 'stun:stun.l.google.com:19302'}]};
const peerConnection = new RTCPeerConnection(configuration);

// ローカルのビデオストリームを取得
navigator.mediaDevices.getUserMedia({ video: true, audio: true })
    .then(stream => {
        localVideo.srcObject = stream;
        stream.getTracks().forEach(track => peerConnection.addTrack(track, stream));
    });

// リモートストリームの設定
peerConnection.ontrack = event => {
    remoteVideo.srcObject = event.streams[0];
};

// シグナリングメッセージの処理
socket.on('message', async message => {
    if (message.type === 'offer') {
        await peerConnection.setRemoteDescription(new RTCSessionDescription(message));
        const answer = await peerConnection.createAnswer();
        await peerConnection.setLocalDescription(answer);
        socket.emit('message', peerConnection.localDescription);
    } else if (message.type === 'answer') {
        await peerConnection.setRemoteDescription(new RTCSessionDescription(message));
    } else if (message.type === 'candidate') {
        await peerConnection.addIceCandidate(new RTCIceCandidate(message.candidate));
    }
});

// ICE候補の処理
peerConnection.onicecandidate = event => {
    if (event.candidate) {
        socket.emit('message', { type: 'candidate', candidate: event.candidate });
    }
};
