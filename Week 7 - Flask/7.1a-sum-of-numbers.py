# Napisz program, który po wejściu na adres: /add/<liczba1>/<liczba2> odpowie sumą podanych liczb.
# Przykład: wejście na /add/3/5 powinno zwrócić "8".

from flask import Flask

app = Flask(__name__)

@app.route("/add/<num1>/<num2>")
def add(num1, num2):
    sum = int(num1) + int(num2)
    return str(sum)

app.run(debug=True)