# Napisz aplikację - na podstawie podanego szablonu - która po podaniu tekstu i liczby zwróci tekst "przesunięty w prawo"
# (uwaga: ograniczamy się do małych liter alfabetu łacińskiego) o liczbę podaną przez użytkownika (np. abcd -> bcde, zdcb -> aedc)
# Przydatne funkcje: chr, ord
# Przydatny operator: % (modulo)
# Przydatna informacja: alfabet łaciński ma 26 liter

from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def cezar_handler():
    if request.method == 'POST':
        word = request.form['text']
        offset = int(request.form['offset'])

        for letter in word:


            return word

    return render_template('cezar.html')

app.run(debug=True)