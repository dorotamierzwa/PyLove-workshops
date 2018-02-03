import requests

data = requests.post(
    'http://localhost:5000/',
    json={'file': 'hehe.txt'}
)

print(data.text)