# Na rozszerz generator z zad 6. tak, żeby zwracał instancję klasy lub namedtuple zwierającą dowcip, id,
# czas stworzenia klasy, czas trwania zapytania.

import requests


def chuck_jokes():
    jokes = requests.get("https://api.icndb.com/jokes/random")
    yield jokes.json()['value']['joke']


for x in chuck_jokes():
    print(x)
