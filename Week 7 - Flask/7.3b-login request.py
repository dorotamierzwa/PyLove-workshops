import requests

login = requests.post(
    'http://localhost:5000/user/dorota/attempt-login',
    json={'input_password': 'my pass'}
)

print(login.text)