# Napisz aplikację - na podstawie podanego szablonu - która po podaniu tekstu i liczby zwróci tekst "przesunięty w prawo"
# (uwaga: ograniczamy się do małych liter alfabetu łacińskiego) o liczbę podaną przez użytkownika (np. abcd -> bcde, zdcb -> aedc)
# Przydatne funkcje: chr, ord
# Przydatny operator: % (modulo)
# Przydatna informacja: alfabet łaciński ma 26 liter

from flask import Flask, request, render_template

app = Flask(__name__)


def cesar_encryption(word, offset):
    encrypted_word = ''
    for character in word:
        if ord(character) >= 97 and ord(character) <= 122:
            encrypted_word += chr((ord(character) + offset + 7) % 26 + 97)

        else:
            encrypted_word += character

    return encrypted_word


@app.route('/', methods=['GET', 'POST'])
def cesar_handler():
    encrypted_text = ''
    if request.method == 'POST':
        offset = int(request.form.get('offset', 0))
        word = request.form.get('text', '')
        encrypted_text = cesar_encryption(word, offset)

    return render_template('cezar.html', encrypted_text=encrypted_text)

app.run(debug=True)
