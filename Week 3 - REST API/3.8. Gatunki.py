# Korzystając z API https://swapi.co/api/. Wyświetl wszystkie nazwy ras gatunków wystepujących w
# V częsci Gwiezdnych Wojen (Imperium kontratakuje).

import requests

empire_strikes_back = requests.get("https://swapi.co/api/films/?search=empire")
empire_results = empire_strikes_back.json()['results']
species = []

for element in empire_results:
    if element['title'] == "The Empire Strikes Back":
        species = element['species']

for specie in species:
    list_of_species = requests.get(specie)
    print(list_of_species.json()['name'])