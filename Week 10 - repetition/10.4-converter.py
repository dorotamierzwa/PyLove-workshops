# Napisz prosty konwerter walut, który na wejściu przyjmie stringa składającego się z:
# kwoty, waluty wejściowej, słówka kluczowego "to" i kwoty wyjściowej.
# Użyj następujących kursów: 1 PLN to 1000 USD, 1 PLN to 4505 EURO, 1 PLN to 100 JPY
# Załóż, że konwersje są wykonywane tylko z lub do PLNów.
# Dla zaawansowanych: przeliczaj wszystkie waluty między sobą (PLN, USD, EURO, JPY)
# Przykład:
# input: "2 PLN to USD" output: "2000 USD"
# input "15 USD to PLN" output: "0.015 PLN"

exchange = input("Please input an amount for exchange as in the example below\n"
               "'2 PLN to USD'\n")


details = exchange.split(' ')
curr1 = details[1]
curr2 = details[-1]
amount = int(details[0])
if curr1 == 'PLN':
    if curr2 == 'USD':
        print(amount * 1000, 'USD')
    if curr2 == 'EUR':
        print(amount * 4505, 'EUR')
    if curr2 == 'JPY':
        print(amount * 100, 'JPY')
elif curr2 == 'PLN':
    if curr1 == 'USD':
        print(amount / 1000, 'PLN')
    if curr1 == 'EUR':
        print(amount / 4505, 'PLN')
    if curr1 == 'JPY':
        print(amount / 100, 'PLN')

