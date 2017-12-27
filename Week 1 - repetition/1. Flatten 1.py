flat_list = []


def flatten(current_list):

    element = current_list.pop(0)

    if isinstance(element, list):
        flatten(element)
    else:
        flat_list.append(element)
    if len(current_list) > 0:
        flatten(current_list)
    return


lista = [['a', [[[['l'], 'p'],'34']]],'i']
flatten(lista)
print(flat_list)