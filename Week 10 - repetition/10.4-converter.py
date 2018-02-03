# Napisz prosty konwerter walut, który na wejściu przyjmie stringa składającego się z:
# kwoty, waluty wejściowej, słówka kluczowego "to" i kwoty wyjściowej.
# Użyj następujących kursów: 1 PLN to 1000 USD, 1 PLN to 4505 EURO, 1 PLN to 100 JPY
# Załóż, że konwersje są wykonywane tylko z lub do PLNów.
# Dla zaawansowanych: przeliczaj wszystkie waluty między sobą (PLN, USD, EURO, JPY)
# Przykład:
# input: "2 PLN to USD" output: "2000 USD"
# input "15 USD to PLN" output: "0.015 PLN"

converter = {
    'USD': 1000, 'EUR': 4505, 'JPY': 100, 'PLN': 1}

def convert(currencies):
    value_in, value_out = currencies.split(' to ')
    # import pdb;
    # pdb.set_trace()
    if value_out == 'PLN':
        amount_in, curr_in = value_in.strip().split(' ')
        amount_out = float(amount_in) / converter.get(curr_in.strip())
    else:
        amount_in, curr_in = value_in.strip().split(' ')
        amount_out = float(amount_in) * converter.get(value_out)

    return print(amount_out, value_out)


convert('15 USD to PLN')
convert('2 PLN to USD')
