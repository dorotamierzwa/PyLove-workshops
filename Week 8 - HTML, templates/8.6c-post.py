# ...jeśli użytkownik wprowadził wartość niebędącą liczbą, powinien zostać wyświetlony komunikat o błędzie.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def sum_num():
    print()
    if request.method == 'GET':
        return render_template('8.6c-get.html')
    elif request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        sum = 0
        if num1 is not None and num2 is not None:
            try:
                sum = int(num1) + int(num2)
            except ValueError:
                return "Wrong input. Please provide numbers only."
        return render_template('8.6c-post.html', num1=num1, num2=num2, sum=sum)


app.run(debug=True)
