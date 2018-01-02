# Napisz program, który po wejściu na adres /current-status metodą POST ustawi aktualny status na podstawie przekazanego
# w zapytaniu JSON-a (np. {"status": "starting"}),
# a po wejściu na ten sam adres metodą GET zwróci aktualny status.

from flask import Flask, request

app = Flask(__name__)
saved_status = "Data"

@app.route("/current-status", methods=['POST'])

def save_status():
    global saved_status
    data = request.get_json()
    saved_status = data["status"]
    return "Status {}".format(data["status"])

@app.route("/read", methods=["GET"])
def read_status():
    return saved_status


app.run(debug=True)