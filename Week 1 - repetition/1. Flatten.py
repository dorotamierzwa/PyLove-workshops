# Napisz funkcję, która przyjmuje strukturę zagnieżdżonych list i spłaszcza ją do płaskiej listy

flat_list = []


def flatten(current_list):

    element = current_list.pop(0)
    if isinstance(element, list):
        flatten(element)
    else:
        flat_list.append(element)
    if len(current_list) > 0:
        flatten(current_list)






lista = [['a', 'b', ['e', ['r', 't', [1, [2, 3], [5, 6, 7]]]], ['e', 'c']], 'd']
flatten(lista)
print(flat_list)


