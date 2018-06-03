# Napisz algorytm, który zmieni wszystkie stopnie Celsujsza na Farenheita w podanej liście: [39.2, 36.5, 37.3, 37.8]

c = [39.2, 36.5, 37.3, 37.8]
fahrenheit = lambda x: (x * 9/5) + 32
f = [fahrenheit(x) for x in c]
print(f)