# Napisz aplikacje we flasku, która wygląda jak główna strona google... po kliknięciu szukaj przekierowuje na:
# "http://thecatapi.com/api/images/get?format=src&type=gif"
# lub na:
# "http://thecatapi.com/api/images/get"

from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def google():
    if request.method == 'POST':
        return redirect('http://thecatapi.com/api/images/get')

    return render_template('google.html')

app.run(debug=True)