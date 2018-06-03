# Rozszerz generator o limit określający ostatni kolejny element.

def fibonacci_nums(n):
    a, b, count = 0, 1, 0
    while True:
        if (count > n): return
        yield a
        a, b = b, a + b
        count += 1

print(list(fibonacci_nums(7)))