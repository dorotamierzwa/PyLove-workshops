# Korzystając z API https://swapi.co/api/. Policz BMI wszystkich pilotów Milenium Falcona I wyswietl je wraz z ich imionami.

import requests

falcon = requests.get("https://swapi.co/api/starships/?search=millennium")

falcon_pilots = falcon.json()['results']
list_of_pilots = []

for element in falcon_pilots:
    if element['name'] == "Millennium Falcon":
        pilots = element['pilots']

for pilot in pilots:
    list_of_pilots = requests.get(pilot)
    print("BMI of", list_of_pilots.json()['name'], "is: ",
           (float(list_of_pilots.json()['mass'])/float(list_of_pilots.json()['mass'])**2))