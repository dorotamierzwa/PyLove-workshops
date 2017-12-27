class Czas:
    def __init__(self, hour, minute=0, second=0):
        self.h = hour
        self.m = minute
        self.s = second

# Zaimplementuj metodę magiczną __str__, która wyświetli aktualne wartości np. <zeg h=0, m=3, s=5>

    def __str__(self):
        temp = "{} ".format(self._get_name())
        for atr in dir(self):
            if not atr.startswith('_') and not callable(getattr(self, atr)):
                temp += "{}={} ".format(atr, getattr(self, atr))
        return temp

    @classmethod
    def _get_name(cls):
        return cls.__name__

# Zaimplementuj metodę set_time, która pozwoli nadpisać aktualne wartości czasu.

    def set_time(self, h=None, m=None, s=None):
        if h:
            self.h = h

        if m:
            self.m = m

        if s:
            self.s = s

    def get_seconds(self):
        sum_seconds = self.m * 60 + self.s + self.h * 60 * 60
        return sum_seconds

    def get_minutes(self):
        sum_minutes = self.m + self.h * 60 + self.s / 60
        return  sum_minutes

    def get_hours(self):
        sum_hours = self.h + self.m / 60 + self.s / (60*60)
        return sum_hours

    def add_time(self, h=None, m=None, s=None):
        if s:
            if self.s + s > 59:
                self.m += 1
                self.s = self.s + s - 60
            else:
                self.s += s

        if m:
            self.m += m
            if self.m // 60 >= 1:
                self.h += self.m // 60
                self.m = self.m % 60

        if h:
            self.h += h

# Stwórz klasę Zegar, która dziedziczy po Czas a konstruktor (__init__) będzie brał obowiązkowo parametr
# format (12H lub 24H) oprócz tych co Czas.

class Zegar(Czas):
    def __init__(self, time_format, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tf = time_format

# Stwórz klasę DokładnyZegar, która dziedziczy po Zegar i która jeszcze będzie przyjmowała opcjonalnie milisekundy.

class DokladnyZegar(Zegar):
    def __init__(self, *args, ms=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.ms = ms

    def set_time(self, ms=None, **kwargs):
        super().set_time(**kwargs)
        if ms:
            self.ms = ms

# Zaimplementuj metodę pozwalającą zwiększyć czas o minutę, sekundę, godzinę, a w przypadku Dokładnego Zegara dodatkowo
# milisekundy. Pamiętaj, że przekraczając 60 minutę lub sekundę powinna też odpowiednio zwiększyć odpowiednio godzinę lub
# minutę.

    def add_time(self, h=None, m=None, s=None, ms=None):
        Czas.add_time(self, h, m, s)

        if ms:
            self.ms += ms
            if self.ms // 1000 >= 1:
                self.s += (self.ms // 1000)
                self.ms = self.ms % 1000

# Napisz swoją wersję printa o nazwie mojprint, która oprócz zwykłych argumentów pobierze jeszcze obowiązkowo ile razy
# dana rzecz ma być wyprintowana oraz opcjonalnie czy ma być jakiś sufix przed daną wartością.

    def mojprint(self, times, sufix=None):
        for i in range(0, times):
            if sufix is not None:
                print(self, sufix)
            else:
                print(self)

zeg = DokladnyZegar('24', 0, 2, 45)
print(zeg)
zeg.add_time(m=65, ms=1200)
print(zeg)
