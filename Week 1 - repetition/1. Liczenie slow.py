# Napisz funkcję, która policzy słowa w tekście. Każde słowo jest oddzielone spacją.


def policz_slowa(text):
    wyrazy = text.split(" ")

    print(len(wyrazy))

policz_slowa("Ala ma kota")
policz_slowa("Pies psu niedzwiedziem, bo tak")
