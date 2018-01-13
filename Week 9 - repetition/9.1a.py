# Napisz aplikację, która po wejściu na adres "/konto" wyświetli stan konta użytkownika i listę ostatnich przelewów.
# Początkowy stan konta ustaw np. na 1000 zł.
# Na stronie powinien znajdować się formularz, umożliwiający wykonanie przelewu - powinien zawierać dwa pola tekstowe:
# * nr konta docelowego,
# * kwotę przelewu.
# Po przesłaniu formularza kwota na koncie powinna zostać zmniejszona o podaną wartość, ponadto nowy przelew powinien
# pojawić się na liście ostatnich przelewów.
# Upewnij się, że odświeżenie strony po wykonaniu przelewu nie spowoduje wykonania tego przelewu jeszcze raz.

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


app.run(debug=True)