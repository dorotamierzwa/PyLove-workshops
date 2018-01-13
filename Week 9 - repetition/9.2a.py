# Napisz aplikację, która będzie wyświetlać dane pracowników pewnej firmy. Każdy pracownik będzie mieć identyfikator,
# imię, nazwisko, płacę, opis stanowiska (użyj klasy po stronie serwera). Utwórz stonę zawierającą tabelę pracowników
# (adres wymyśl samodzielnie). W każdym wierszu tabeli powinny znaleźć się imię, nazwisko pracownika i dodatkowa pusta
# komórka - uzupełnimy ją w następnym zadaniu.

from flask import Flask, render_template

app = Flask(__name__)


class Employee:
    def __init__(self, id, fname, lname, pay, position):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.position = position


table_emp = [
    Employee(1, 'Barack', 'Obama', 2000, 'President'),
    Employee(2, 'Krzystof', 'Kuc', 6777, 'CEO'),
    Employee(3, 'Julia', 'Roberts', 15000, 'Actress'),
    Employee(4, 'Johnny', 'Depp', 1309, 'Pirate')
]


@app.route('/people', methods=['GET'])
def people_list():
    return render_template('9.2a-people.html', table_emp=table_emp)


app.run(debug=True)
