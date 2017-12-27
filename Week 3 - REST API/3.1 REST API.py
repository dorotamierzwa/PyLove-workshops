# Korzystając z API http://py.net/ zmień status (/status/set) i sprawdź czy się udało (/status)

import requests
resp = requests.get('http://py.net/status')
print(resp.json())

resp = requests.post(
    'http://py.net/status/set',
    json={
        "status": "Nowy status"
    }
)

resp = requests.get('http://py.net/status')
print(resp.json())