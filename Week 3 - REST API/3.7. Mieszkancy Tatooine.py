import requests

tatooine = requests.get("https://swapi.co/api/planets/1")

print(tatooine.json()['residents'])

for x in tatooine.json()['residents']:
    person = requests.get(x)
    print(person.json())


