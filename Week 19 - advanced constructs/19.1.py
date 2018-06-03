# Pobierz losowe dane z https://pylove.org/exercise/1_19_1 i ułóż hasło tylko z unikalnych słów.

import requests

my_set = set(requests.get('https://pylove.org/exercise/1_19_1').json())

for el in my_set:
    if el.isalpha():
        print(el)



