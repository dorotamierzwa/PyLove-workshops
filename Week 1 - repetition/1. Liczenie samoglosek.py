# Napisz funkcję, która policzy wszystkie samogłoski w tekście.

def policz_samogloski(text):
    vowels = 0
    for i in text:
        if i in "aeiouAEIOU":
            vowels += 1
    print(vowels)

policz_samogloski("Ala ma kota")
policz_samogloski("Pies psu niedzwiedziem")