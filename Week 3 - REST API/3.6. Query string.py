import requests

resp = requests.get("http://py.net/query_string?parsefhgd")


print(resp.json())