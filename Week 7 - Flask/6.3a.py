# Napisz program, który: po wejściu na adres /user/<username>/set-password ustawi hasło użytkownika username
# (na podstawie podanego JSON-a).

from flask import Flask, request

app = Flask(__name__)
password = "data"

@app.route("/user/<username>/set-password", methods=['POST'])

def set_password(username):
    global password
    data = request.get_json()
    password = data["password"]
    return "Password {}".format(data["password"])

@app.route("/user/<username>/show-password", methods=["GET"])
def show_password(username):
    return password

app.run(debug=True)

