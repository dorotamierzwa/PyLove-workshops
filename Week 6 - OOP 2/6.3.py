# Stwórz klasę DokładnyZegar, która dziedziczy po Zegar i która jeszcze będzie przyjmowała opcjonalnie milisekundy.

class Czas:
    def __init__(self, hour, minute=0, second=0):
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


class Zegar(Czas):
    def __init__(self, time_format, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tf = time_format


class DokladnyZegar(Zegar):
    def __init__(self, *args, ms=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.ms = ms



def mojprint():
    pass

dzeg = DokladnyZegar(12, 15, 8, 4, ms=8)
print('h:', dzeg.h)
print('m:', dzeg.m)
print('s:', dzeg.s)
print('ms:', dzeg.ms)
print('time format:', dzeg.tf)


