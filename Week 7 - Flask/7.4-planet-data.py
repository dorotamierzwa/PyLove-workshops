# Napisz program, który po wejściu na adres /planet-details?planet=Tatooine odpowie jsonem zawierającym dane planety,
# o którą zapytał użytkownik (np. klimat, liczba mieszkańców). Dane planety program powinien pobierać ze Star Wars API,
# np.: https://swapi.co/api/planets/?search=Tatooine


from flask import Flask, request
import requests
import json


app = Flask(__name__)


@app.route("/planet-details", methods=['GET'])
def planet_data():
    planet = request.args['planet']
    data = requests.get("https://swapi.co/api/planets/?search=" + planet)
    planet_results = data.json()['results']

    if not planet_results:
        return "Planet {} does not exist.".format(planet)

    planet_data = planet_results[0]
    return json.dumps(planet_data)


app.run(debug=True)
