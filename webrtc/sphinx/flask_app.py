from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="buiid/html")


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/_static/<path:filename>")
def css(filename):
    return send_from_directory(f"{app.static_folder}/_static", filename)


@app.route("/_static/<path:filename>")
def js(filename):
    return send_from_directory(f"{app.static_folder}/_static", filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
