# Aplikację z punktu 1a. zmodyfikuj tak, aby po wejściu na adres "/" użytkownik został przekierowany na adres "/konto".

from flask import Flask, request, render_template, redirect

app = Flask(__name__)


transactions = []
balance = 1000

@app.route('/account', methods=['GET', 'POST'])
def bank_account():

    if request.method == 'POST':
        global balance
        account_number = request.form.get('account_number')
        transfer = int(request.form.get('transfer'))
        balance -= transfer
        transactions.append({'account_number': account_number, 'transfer': transfer})
        return redirect('/account')

    return render_template('9.1a-template.html', transactions=transactions, balance=balance,)

@app.route("/")
def back_to_acc():
    return redirect("/account")


app.run(debug=True)