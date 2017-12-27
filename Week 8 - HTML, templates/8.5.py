# Przykład formularza z lekcji zmodyfikuj tak, aby formularz wysyłał zapytanie POST zamiast GET
# (program ma nadal działać tak jak wcześniej).

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/search", methods=['GET', 'POST'])
def search():
    query = request.form.get('query')
    return render_template('formularz.html', query=query)

app.run(debug=True)