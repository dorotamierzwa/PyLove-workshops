# Napisz funkcję, która sprawdzi, czy liczba znaków "x" i "o" w stringu jest taka sama i zwróci True/False.
# Jeśli string zawiera coś innego niż "x" lub "o", to wypisze błąd.

def xo_counter(text):
    x_count = 0
    o_count = 0
    for i in text:
        if i in "xX":
            x_count += 1
        elif i in "oO":
            o_count += 1
        else:
            print("Illegal letters in text")
            return
    if x_count == o_count:
        print(True)
    else: print(False)

xo_counter("xoxoxox")