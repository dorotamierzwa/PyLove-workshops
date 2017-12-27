# Utwórz klasę Osoba. Każda instancja tej klasy powinna posiadać trzy atrybuty – imię, nazwisko i wiek.
# Utwórz listę kilku dowolnych osób. Utwórz szablon HTML, który będzie renderował tabelę osób (imię, nazwisko i wiek
# powinny wyświetlać się w osobnych kolumnach). Napisz program, który po wejściu na adres /osoby renderuje ten szablon.
# Przetestuj program w przeglądarce.

class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek


@app.route("/osoby")
def lista_osob():
