# Stwórz - z wykorzystaniem klas i dziedziczenia - kalkulator objętości brył:
# sześcianu, prostopadłościanu, stożka i walca.
# Powinien on wczytać od użytkownika opcję (0, 1, 2 lub 3) i w zależności od tego przyjąć
# 3 argumenty, 2 lub 1 i obliczyć objętość. Na wszelki wypadek wzory na objętość podane poniżej.
# Sześcian: V = a^3
# Prostopadłościan: V = a*b*c
# Kula: V = 4/3 * pi * r^3

from math import pi

class Szescian():
    def __init__(self, a):
        self.a = a

    def obj_szesc(self):
        return print("Objetosc szescianu wynosi", self.a ** 3)

class Prostopadloscian(Szescian):
    def __init__(self, b, h, *args):
        self.b = b
        self.h = h
        super(Prostopadloscian, self).__init__(*args)

    def obj_prost(self):
        return print("Objetosc prostopadloscianu wynosi", self.a * self.b * self.h)

class Stozek():
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def obj_stoz(self):
        return print("Objetosc stozka wynosi", self.h * pi * 1/3 * self.r)

class Walec(Stozek):
    def __init__(self, *args):
        super(Walec, self).__init__(*args)

    def obj_wal(self):
        return print("Objetosc walca wynosi", self.h * pi * self.r)


choice = input("Podaj jaka bryle chcesz policzyc:\n"
      "1 - Szescian\n"
      "2 - Prostopadloscian\n"
      "3 - Stozek\n"
      "4 - Walec\n")

if choice == '1':
    a = int(input("Bok a: "))
    sz1 = Szescian(a)
    sz1.obj_szesc()

elif choice == '2':
    a = int(input("Bok a: "))
    b = int(input("Bok b: "))
    h = int(input("Wysokosc: "))
    p1 = Prostopadloscian(a, b, h)
    p1.obj_prost()

elif choice == '3':
    r = int(input("Promien: "))
    h = int(input("Wysokosc: "))
    s1 = Stozek(r, h)
    s1.obj_stoz()

elif choice == '4':
    r = int(input("Promien: "))
    h = int(input("Wysokosc: "))
    w1 = Walec(r, h)
    w1.obj_wal()

else:
    print("Invalid input")