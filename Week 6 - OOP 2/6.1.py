# Stwórz klasę Czas, której konstruktor (__init__) będzie brał trzy opcjonalne argumenty, godzine, minuty,
# sekundy i zapisywal je w odpowiednich zmiennych w klasie.

class Czas:
    def __init__(self, hour=0, minute=0, second=0):
        self.h = hour
        self.m = minute
        self.s = second

    def __str__(self):
        pass

    def set_time(self):
        pass

    def add_time(self):
        pass

    def get_seconds(self):
        pass

    def get_minutes(self):
        pass

    def get_hours(self):
        pass


class Zegar:
    pass

class DokładnyZegar:
    pass



def mojprint():
    pass

n_czas = Czas(1, 2, 3)
print(n_czas.h)
print(n_czas.m)
print(n_czas.s)