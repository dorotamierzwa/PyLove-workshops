# Korzystając z API http://py.net/ ściągnij i zapisz na dysku losowe zdjęcia kotów (/cat)

import requests

resp = requests.get("http://py.net/cat")

with open("file.jpg", "wb") as cat:
    cat.write(resp.content)
