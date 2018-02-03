# Napisz program, który w zależności od opcji podanej przez użytkownika (1, 2 lub 3)
# odczyta odpowiednio plik x.txt, y.txt lub z.txt (zawartość dowolna)
# obsługa błędów powinna obejmować (co najmniej) komunikat o nieprawidłowej opcji,
# zaś wczytywanie treści pliku powinno znaleźć się w oddzielnej funkcji (wraz z obsługą błędów)


def load_file(opt):
    available_files = {'1': 'x', '2': 'y', '3': 'z'}
    try:
        filename = '{}.txt'.format(available_files[opt])
        with open(filename, 'r') as f:
            return f.read()

    except KeyError:
        return None


success = False

while not success:
    opt = input('Choose a file to open.')
    content = load_file(opt)
    if content:
        success = True
        print('Wow I loaded: {}'.format(content))
    else:
        print('I don\'t know this one')
