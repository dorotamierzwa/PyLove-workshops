# ...po wejściu na /user/<username>/login odpowie komunikatem "Login successful" jeśli podane w JSON-ie hasło zgadza się
# z wcześniej ustawionym lub – jeśli hasło się nie zgadza albo w ogóle nie zostało ustawione – komunikatem "Wrong password".


from flask import Flask, request

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

@app.route("/user/<username>/login", methods=["POST"])
def login(username):
    data = request.get_json()
    new_password = data['password']

    if password == new_password:
        return "Login successful"
    else:
        return "Wrong password"

app.run(debug=True)