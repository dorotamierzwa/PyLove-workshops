# Napisz funkcję, która policzy drogę pokonaną przez samochód w czasie t i przyspieszeniu a z opcjonalną prędkością początkową, domyślnie równą 0.

def droga(t, a, v = 0):
    d = (a * t **2)/2 + v * t
    print(d)


droga(5, 5)
droga(10, 10, 100)




