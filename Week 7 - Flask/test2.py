import requests

save_result = requests.post(
    'http://localhost:5000/save',
    json={'value': 'witam'}
)