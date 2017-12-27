# Korzystając z API http://py.net/ pobierz klucz API (api_key) - zaloguj się (/auth).

import requests
resp2 = requests.get('http://py.net/auth')

resp2 = requests.post(
    'http://py.net/auth',
    json={
        "name": "Dorota Mierzwa",
        "password": "pylady"
    }
)

print(resp2.json())