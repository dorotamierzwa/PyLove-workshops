# Napisz funkcję, która znajdzie liczbę odważników o wadze A aby zrównoważyć szale wagi z odważnikami o wadze B

import math

def odwazniki(a, b):
    c = math.gcd(a, b)
    a = a / c
    b = b / c
    print(b, a)


odwazniki(2, 8)
odwazniki(4, 6)