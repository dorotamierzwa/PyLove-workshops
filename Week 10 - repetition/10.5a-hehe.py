# Napisz aplikację, która w zależności od argumentu "file" (GET) odczyta plik "hehe.txt",
# "heheszki.json" lub "beczka_smiechu.txt" (zawartość dowolna, powinny znajdować się w katalogu z aplikacją).
# Obsłuż sytuację, w której plik nie będzie istniał.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/open/<name>', methods=['GET'])
def hehe(name):
    name = str(name)
    if name == 'hehe':
        with open('hehe.txt') as file:
            text = file.readline()
            return render_template('hehe.html', name=name, text=text)
    elif name == 'heheszki':
        with open('heheszki.json') as file:
            text = file.readline()
            return render_template('hehe.html', name=name, text=text)
    elif name == 'beczka-smiechu':
        with open('beczka-smiechu.txt') as file:
            text = file.readline()
            return render_template('hehe.html', name=name, text=text)
    elif ValueError:
        return "Nie ma tu nic heh"

app.run(debug=True)