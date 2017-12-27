# Wczytaj plik i stwórz słownik w którym kluczem będzie imię (i nazwisko) a wartością będzie słownik z kluczami kolor oczu i wzrost

import pprint

file = open('file1.txt')
dictionary = file.readlines()

full_list = {}

for x in dictionary:
    x = x.split(' ')
    if len(x) == 9:
        name = x[1]

    elif len(x) == 10:
        name = " ".join(x[1:3])

    elif len(x) == 11:
        name = " ".join(x[1:4])
    else:
        print(x)
    full_list[name] = {}

    eyes = x[-6]
    height = " ".join(x[-3:-1])

    full_list[name] = {'height' : height, 'eyes' : eyes}

pprint.pprint(full_list)
