# Napisz funkcję która zamieni czas na sekundy, minuty lub godziny.
# Jako wejście powinna przyjmować czas w formie "HH:MM:SS" oraz 's', 'm' lub 'h',
# w zależności na jaki format ma przeliczyć czas.

def time_calculation(hour, format):
    a = hour.split(':')
    h = float(a[0])
    m = float(a[1])
    s = float(a[2])

    if format == 'h':
        time = h + m/60
    elif format == 'm':
        time = h * 60 + m
    elif format == 's':
        time = h * 60 * 60 + m * 60 + s
    print(time)


time_calculation('2:00:00', 'h')
time_calculation('2:00:00', 's')
time_calculation('12:00:00', 'm')
time_calculation('1:15:00', 'h')