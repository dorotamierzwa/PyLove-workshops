# Napisz program, który po wejściu na adres /planet-details?planet=Tatooine odpowie jsonem zawierającym dane planety,
# o którą zapytał użytkownik (np. klimat, liczba mieszkańców). Dane planety program powinien pobierać ze Star Wars API,
# np.: https://swapi.co/api/planets/?search=Tatooine


from Flask import flask, requests
import json

app = Flask(__name__)

@app.route("/planet-details?planet=Tatooine")
