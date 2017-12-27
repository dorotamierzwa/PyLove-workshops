import requests

save_result = requests.post(
    'http://localhost:5000/current-status',
    json={'status': 'starting'}
)