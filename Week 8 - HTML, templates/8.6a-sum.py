# Utwórz formularz zawierający dwa inputy o nazwach "liczba1" i "liczba2" oraz przycisk do wysłania formularza.
# Wysłanie formularza metodą GET powinno spowodować wyświetlenie strony zawierającej sumę liczb wprowadzonych przez użytkownika.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def sum_num():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    sum = 0
    if num1 is not None and num2 is not None:
        sum = int(num1) + int(num2)
    return render_template('8.6a-sum.html', num1=num1, num2=num2, sum=sum)


app.run(debug=True)
