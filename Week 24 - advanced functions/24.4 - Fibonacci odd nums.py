# Napisz algorytm, który wyświetli wszystkie nieparzyste liczby w pierwszych 100 elementach ciągu Fibonaciego.

def fibonacci_nums(n):
    a, b, count = 0, 1, 0
    while True:
        if (count > n): return
        yield a
        a, b = b, a + b
        count += 1


fibonacci_odd = [x for x in list(fibonacci_nums(100)) if x % 2 == 1]
print(fibonacci_odd)