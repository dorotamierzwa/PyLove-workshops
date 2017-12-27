import requests

login = requests.post(
    'http://localhost:5000/user/dorota/login',
    json={'password': 'my pass'}
)

print(login.text)