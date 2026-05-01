from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return {"status": "ok", "message": "Hello DevOps"}, 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
