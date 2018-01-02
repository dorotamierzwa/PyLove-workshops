#  Zabezpiecz przed sytuacją, w której użytkownik poda ciąg znaków zamiast liczby.

from flask import Flask

app = Flask(__name__)

@app.route("/add/<num1>/<num2>")
def add(num1, num2):
    try:
        sum = int(num1) + int(num2)
        return str(sum)
    except ValueError:
        return "Wrong input, only integers are accepted!"

app.run(debug=True)