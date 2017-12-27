import requests

tatooine = requests.get("https://swapi.co/api/planets/?search=tatooine")
residents = []

tatooine_results = tatooine.json()['results']

for element in tatooine_results:
    if element['name'] == "Tatooine":
        residents = element['residents']

for resident in residents:
    resident_respone = requests.get(resident)
    print(resident_respone.json())
