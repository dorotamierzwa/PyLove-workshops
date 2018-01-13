# Utwórz klasę Osoba. Każda instancja tej klasy powinna posiadać trzy atrybuty – imię, nazwisko i wiek.
# Utwórz listę kilku dowolnych osób. Utwórz szablon HTML, który będzie renderował tabelę osób (imię, nazwisko i wiek
# powinny wyświetlać się w osobnych kolumnach). Napisz program, który po wejściu na adres /osoby renderuje ten szablon.
# Przetestuj program w przeglądarce.

from flask import Flask, render_template

app = Flask(__name__)


class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age


people_list= [
    Person('Jack', 'Sparrow', 40),
    Person('James', 'Bond', 50),
    Person('Jackie', 'Chan', 45)]


@app.route('/osoby')
def table_data():
    return render_template('table_data.html', people_list=people_list)

app.run(debug=True)