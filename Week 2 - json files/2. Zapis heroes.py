# Zapisz plik sw_all_heros z bohaterami w zdaniach: <Imie> wazy <waga> kg jest <plec> i pochodzi z <Planeta>.
# Przykład: Anakin Skywakaer waży 90 kg jest mężczyzną i pochodzi z Tatuin.


import json

file = open("file_json.json", "r")
data = json.loads(file.read())

sw_all_heroes = open("sw_all_heroes.json", "w", encoding = 'utf-8')

a = 0

for person in data:
    if data[a]['gender'] == "male":
        data[a]['gender'] = "mężczyzną"
    elif data[a]['gender'] == "female":
        data[a]['gender'] = "kobietą"

    description = (data[a]['name'], " waży ", data[a]['mass'], " kg. Jest ", data[a]['gender'], " i pochodzi z ", data[a]['homeworld'], ".")

    a += 1

    sw_all_heroes.writelines(description)
    sw_all_heroes.writelines("\n")

file.close()
sw_all_heroes.close()