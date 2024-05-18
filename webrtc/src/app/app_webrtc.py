from flask import Flask, render_template
from flask_socketio import SocketIO
import os

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def index():
    print("Template folder:", app.template_folder)  # テンプレートフォルダのパスを出力
    return render_template("index.html")


@socketio.on("message")
def handle_message(message):
    socketio.emit("message", message, broadcast=True)


if __name__ == "__main__":
    # Flaskのテンプレート検索パスを出力
    print("Template search paths:")
    for path in app.jinja_loader.searchpath:
        print(path)

    socketio.run(app, host="0.0.0.0", port=6000, debug=True)
