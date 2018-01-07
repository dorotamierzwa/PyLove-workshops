# Napisz program, który po wejściu na adres /hello?name=<imie> odpowie stroną HTML zawierającą nagłówek o treści "Hello <imie>"!

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def hello():
    imie = request.args['name']
    return render_template('imie.html', query=imie)

app.run(debug=True)