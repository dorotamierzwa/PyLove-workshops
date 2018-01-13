# Do aplikacji dodaj stronę wyświetlającą wszystkie informacje o danym pracowniku.
# W ostatniej kolumnie tabeli z zadania 2a powinny pojawić się linki do stron z detalami poszczególnych użytkowników.
# Podpowiedź – w adresie strony z detalami przekaż identyfikator pracownika.


from flask import Flask, render_template

app = Flask(__name__)


class Employee:
    def __init__(self, ide, fname, lname, pay, position):
        self.ide = ide
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.position = position

table_emp = [
    Employee(1, 'Barack', 'Obama', 2000, 'President'),
    Employee(2, 'Krzysztof', 'Kuc', 6777, 'CEO'),
    Employee(3, 'Julia', 'Roberts', 15000, 'Actress'),
    Employee(4, 'Johnny', 'Depp', 1309, 'Pirate')
]


@app.route('/people', methods=['GET'])
def people_list():
    return render_template('9.2a-people.html', table_emp=table_emp)


@app.route('/people/<ide>')
def person_details(ide):
    ide = int(ide)
    for employee in table_emp:
        if employee.ide == ide:
            return render_template('9.2b.html', ide=ide, table_emp=table_emp, employee=employee)


app.run(debug=True)
