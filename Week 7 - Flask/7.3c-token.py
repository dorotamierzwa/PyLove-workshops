# (Do domu) ...po wejściu na /user/<username>/login aplikacja powinna zwracać token w formacie UUID4.

from flask import Flask, request
import uuid

app = Flask(__name__)
password = "data"


@app.route("/user/<username>/set-password", methods=["POST"])
def set_password(username):
    global password
    data = request.get_json()
    password = data["password"]
    return "Password {}".format(data["password"])


@app.route("/user/<username>/show-password", methods=["GET"])
def show_password(username):
    return password


@app.route("/user/<username>/attempt-login", methods=["POST"])
def login(username):
    global new_password
    new_data = request.get_json()
    new_password = new_data['input_password']
    return "Password {}".format(new_data['input_password'])


@app.route("/user/<username>/login", methods=['GET'])
def check_login(username):
    if password == new_password:
        return "Login successful" + str(uuid.uuid4())
    else:
        return "Wrong password"

app.run(debug=True)