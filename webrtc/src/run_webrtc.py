from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def index():
    print("Template folder:", app.template_folder)  # テンプレートフォルダのパスを出力
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=6000, debug=True)
