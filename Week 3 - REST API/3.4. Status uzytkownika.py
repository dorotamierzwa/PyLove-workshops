# Korzystając z API http://py.net/ po pobraniu klucza API (api_key) ustaw status swojego użytkownika (/user_status/set)
# i sprawdź status innych (/user_status) w szczególności koleżanki/kolegi obok.

import requests

resp4 = requests.get("http://py.net/user_status")

resp4 = requests.post(
    "http://py.net/user_status/set",
    json={
        "api_key": "978dd854c4f39e3c9a76df43dbc8d733decd018b2b772800609495402b507c22",
        "status": "I'm yellow"
    }
)

resp5 = requests.get("http://py.net/user_status")

resp5 = requests.get(
    "http://py.net/user_status"
)

print(resp4.json())
print(resp5.json())
