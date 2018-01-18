# Napisz program, który w zależności od opcji podanej przez użytkownika (1, 2 lub 3)
# odczyta odpowiednio plik x.txt, y.txt lub z.txt (zawartość dowolna)
# obsługa błędów powinna obejmować (co najmniej) komunikat o nieprawidłowej opcji,
# zaś wczytywanie treści pliku powinno znaleźć się w oddzielnej funkcji (wraz z obsługą błędów)


choice = input("Which file to open? \n"
                "1. x.txt \n"
                "2. y.txt \n"
                "3. z.txt \n"
                "Choose a number:")

if choice == "1":
    file = open('x.txt', 'r')
elif choice == "2":
    file = open('y.txt', 'r')
elif choice == "3":
    file = open('z.txt', 'r')

def read_file():
    try:
        print("Your content is below: \n", file.readlines())
    except:
        print("No such file in the directory.")


read_file()
