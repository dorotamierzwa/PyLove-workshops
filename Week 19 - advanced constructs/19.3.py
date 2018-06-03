# Dodaj do zadań 1., 2. wyświetlanie czasu rozpoczęcia oraz zakończenia skryptu oraz czas jego wykonania.

from datetime import datetime
import requests

start = datetime.now()
print(start)

my_set = set(requests.get('https://pylove.org/exercise/1_19_1').json())

for el in my_set:
    if el.isalpha():
        print(' '.join(el))

end = datetime.now()
print(end)

print(end - start)
