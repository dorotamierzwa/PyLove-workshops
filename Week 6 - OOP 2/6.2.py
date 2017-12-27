# Stwórz klasę Zegar, która dziedziczy po Czas a konstruktor (__init__) będzie brał obowiązkowo parametr
# format (12H lub 24H) oprócz tych co Czas.

class Czas:
    def __init__(self, hour, minute=0, second=0):
        self.h = hour
        self.m = minute
        self.s = second

    def __str__(self):
        return 'ffhgfh'

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


class DokładnyZegar:
    pass



def mojprint():
    pass

zeg = Zegar('12H', 12, 20, 55)
print(zeg.h)
print(zeg.tf)
print(zeg)
