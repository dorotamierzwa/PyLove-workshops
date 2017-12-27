# Korzystając z API https://swapi.co/api/. Wyświetl imiona wszytkich Gunganów w języku Wooki.

import requests

gungans = requests.get("https://swapi.co/api/species/?format=Wookiee")

names = gungans.json()

gungan_list = []

for gungan in names:
    if gungan['name'] == "Gungan":
        gungan_list = gungan['people']

for person in gungan_list:
    final_list = requests.get(person)
    print(final_list.json())
