# Wczytaj zawarty w pliku json. Stwórz plik który będzie posiadał wszystkie statki w zdaniach od najdroższego do najtańszego:
# <Nazwa> kosztuje <123> credits.


import json
from operator import itemgetter

file1 = open("Statki.json", "r")
ships = json.loads(file1.read())
statki = open("Statki_abc.json", "w", encoding='utf-8')

list_of_ships = []

a = 0

for ship in ships:
    description = []
    # name = ships[a]['name']
    # cost = ships[a]['cost_in_credits']
    description.append(ships[a]['name'])

    if ships[a]['cost_in_credits'] != "unknown":
        description.append(int(ships[a]['cost_in_credits']))
    else:
        description.append(0)  # "unknown" costs saved as integers

    list_of_ships.append(description)
    a += 1

sorted_ships = sorted(list_of_ships, key=itemgetter(1), reverse=True)

b = 0
for x in sorted_ships:
    if sorted_ships[b][1] == 0:
        y = (str(sorted_ships[b][0]) + " kosztuje n/a credits.\n")  # change from 0 to n/a
    else:
        y = (str(sorted_ships[b][0]) + " kosztuje " + str(sorted_ships[b][1]) + " credits.\n")
    b += 1
    statki.writelines(y)
