# Napisz aplikację, która w zależności od argumentu "file" (GET) odczyta plik "hehe.txt",
# "heheszki.json" lub "beczka_smiechu.txt" (zawartość dowolna, powinny znajdować się w katalogu z aplikacją).
# Obsłuż sytuację, w której plik nie będzie istniał.

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def loading():

    data = request.get_json()
    filename = data['file']

    try:
        with open(filename, 'r') as f:
            content = f.read()
        return content

    except FileNotFoundError:
        return "Cannot load such file"


app.run(debug=True)
