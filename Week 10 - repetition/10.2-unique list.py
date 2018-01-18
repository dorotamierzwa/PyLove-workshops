# Napisz algorytm, który na wejście przyjmie listę zawierającą tylko stringi i integery.
# Zwróci listą zawierającą tylko powtarzające się wartości, nie zmieniając ich kolejności.
# Przykład: [1, 2, 3, 1, 3] 1 i 3 nie są unikalne, więc wynikiem będzie [1, 3, 1, 3].

user_input = input("Please provide a sequence of characters:")

user_list = list(user_input)
single_vals = []


for element in user_list:
    if user_list.count(element) == 1:
        single_vals.append(element)


for single_val in single_vals:
    user_list.remove(single_val)

print(user_list)
