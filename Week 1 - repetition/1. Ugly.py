# Funkcja, która sprawdza, czy liczba jest brzydka (i wypisze True). Liczby brzydkie to te,
# które dzielą się przez 2, 3, 5. Liczba 1 też jest brzydka.

def ugly_number(a):
    if a % 5 == 0:
        print(True)
    elif a % 3 ==0:
        print(True)
    elif a % 2 == 0:
        print(True)
    elif a == 1:
        print(True)
    else:
        print(False)


ugly_number(15)
ugly_number(12)
ugly_number(11)
ugly_number(1)