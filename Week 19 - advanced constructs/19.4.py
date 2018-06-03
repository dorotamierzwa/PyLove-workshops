# Wykonaj zadanie 2. z wykorzystaniem konstruktu Counter z biblioteki collections.

from collections import Counter
import requests

data = requests.get('https://pylove.org/exercise/1_19_2').text

c = Counter(data)
c = c.most_common(6)
password = ''

for k, v in c:
    password += k

print(password)

