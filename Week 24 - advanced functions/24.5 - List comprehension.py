# Napisz list comprehension, która będzie zawierała tylko całkowite dodatnie liczby z
# listy [134.6, -2203.4, 344, 68.3, -112, 344, 1212.712]

l = [134.6, -2203.4, 344, 68.3, -112, 344, 1212.712]

new_l = [num for num in l if num > 0 and num % 1 == 0]

print(new_l)