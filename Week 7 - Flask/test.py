from flask import Flask, request

app = Flask(__name__)

saved = "Data"

@app.route("/save", methods=["POST"])
def save():
    global saved
    data = request.get_json()
    saved = data["value"]
    return "Saved {}".format(data["value"])

@app.route("/read", methods=["GET"])
def read():
    return saved

app.run(debug=True)