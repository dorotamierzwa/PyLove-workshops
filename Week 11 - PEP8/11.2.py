"""
PyLove PEP8 & pylint exercise
"""


def podzielna(liczba, podzielna_przez):
    """
    funkcja sprawdzająca podzielność
    :param liczba:
    :param podzielna_przez:
    :return:
    """
    return liczba % podzielna_przez == 0


def ugly(liczba):
    """
    funkcja sprawdzająca czy liczba jest brzydka
    """
    try:
        if liczba == 1:
            return True
        for i in [2, 3, 5]:
            if podzielna(liczba, i):
                return True
        return False
    except ValueError:
        import pdb
        pdb.set_trace()


print(ugly("12"))
print(ugly(12))


def time(czas, jednostka):
    """
    funkcja zegar
    """
    hour, minute, sec = czas.split(':')
    hour = int(hour)
    minute = int(minute)
    sec = int(sec)
    if jednostka == 'sec':
        return hour * 3600 + minute * 60 + sec
    elif jednostka == 'minute':
        return hour * 60 + minute + round(sec / 60, 2)
    return hour + round(minute / 60, 2) + round(sec / 3600, 2)


print(time('01:15:59', 's'))
print(time('01:15:59', 'm'))
print(time('01:15:59', 'h'))

RESULT = []
RESULT_2 = []


def flatten(arr):
    """
    funkcja spłaszczająca listę
    """
    for element in arr:
        if isinstance(element, list):
            flatten(element)
        else:
            RESULT.append(element)
        return RESULT


def flatten_nr(arr):
    """
    :param arr: argument
    :return:
    """
    while True:
        element = arr.pop()
        if not isinstance(element, list):
            RESULT_2.append(element)
        else:
            arr = element
        if arr:
            break
    return RESULT_2[::-1]


print(flatten([[[[[[[[[['a'], 'b']]], 'c']]], 'd']], 'e']))
print(flatten_nr([[[[[[[[[['a'], 'b']]], 'c']]], 'd']], 'e']))


def weird_power(num):
    """
    :param num:
    :return:
    """
    return num ** 2, num ** 3


def calculate(afun, data):
    """
    :param afun:
    :param data:
    :return:
    """
    return afun(weird_power(data))


def suma_b(num):
    """
    :param num:
    :return:
    """
    return sum(num)


A = 3
D = A + 4
F = calculate(D, A)
print(F)


def power_2(num):
    """
    :param num:
    :return:
    """
    return (num + 0.5 * num) ** 2


print(power_2(3))

X = (A + 0.5 * A) ** 2
print(X * 3)


DATA = [(9, 0), (1, 2), (3, 4)]
SORTED_DATA = sorted(DATA, key=lambda num: num[0], reverse=False)
MAX_DATA = max(DATA[0])
MIN_DATA = min(DATA[0])


print({
    'a': {
        'a': {
            'a': {
                'a': {
                    'a': {
                        'a': {
                            'a': {
                                'a': {
                                    'a': {
                                        'a': {
                                            'a': {
                                                'a': {
                                                    'a': {
                                                        'a': {
                                                            'a': {
                                                                'a': {
                                                                    'a': {
                                                                        'a': {
                                                                            'a': {
                                                                                'a': {
                                                                                    'a': {
                                                                                        'a': {
                                                                                            'a': 1
                                                                                        }
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

        }
    }
})
