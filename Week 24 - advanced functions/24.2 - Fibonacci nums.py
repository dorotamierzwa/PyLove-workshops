# Napisz generator kolejnych wartości ciągu Fibonaciego.

def fibonacci_nums():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print(list(fibonacci_nums()))


# def szesciany_kolejne(start, end):
#     for i in range(start, end):
#         yield i ** 3
#
#
# # Przykład użycia
#
# x_3 = szesciany_kolejne(3, 60)
# print(x_3)  # <generator object szesciany_kolejne at 0x10eb74678>
# for x in x_3:
#     print(x)
# print(list(x_3))  # pusta lista