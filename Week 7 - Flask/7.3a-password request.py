import requests

save_password = requests.post(
    'http://localhost:5000/user/dorota/set-password',
    json={'password': 'my pass'}
)

print(save_password.text)