# Korzystając z API http://py.net/ zarejestrój się (/register) pamiętaj że może być tylko jeden użytkownik pod daną nazwą (name)

import requests
resp1 = requests.get('http://py.net/register')

resp1 = requests.post(
    'http://py.net/register',
    json={
        "name": "Dorota Mierzwa",
        "password": "pylady"
    }
)

print(resp1.json())