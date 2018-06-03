# Wykorzystując https://api.icndb.com/jokes/1 lub https://api.icndb.com/jokes/random
# (dokumentacja: http://www.icndb.com/api/) napisz generator, który będzie zwracał kolejne żarty o Chucku Norrisie
# w formie stringa, aż się nie wyczerpią.

import requests


def chuck_jokes():
    while True:
        jokes = requests.get("https://api.icndb.com/jokes/random")
        yield jokes.json()['value']['joke']


for x in chuck_jokes():
    print(x)
