# Napisz program, który po wejściu na adres: /add/<liczba1>/<liczba2> odpowie sumą podanych liczb.
# Przykład: wejście na /add/3/5 powinno zwrócić "8".

from flask import Flask

app = Flask(__name__)

@app.route("/add/<liczba1>/<liczba2>")
def add(liczba1, liczba2):
    suma = int(liczba1) + int(liczba2)
    return str(suma)

app.run(debug=True)