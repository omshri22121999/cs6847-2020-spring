from flask import Flask, Response

app = Flask(__name__)


@app.route("/count")
def count():
    with open("count.txt", "r") as f:
        a = f.read()
    resp = Response(a)
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


@app.route("/fp")
def fp():
    with open("frequent_items.txt", "r") as f:
        a = f.read()
    resp = Response(a)
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

