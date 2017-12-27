#Znajdź i zapisz wszystkie imiona kobiet do pliku sw_women a wszystkich mężczyzn do sw_men

import json

sw_women = open("sw_women.json", "w", encoding = 'utf-8')
sw_men = open("sw_men.json", "w", encoding = 'utf-8')

file = open("file_json.json", "r")
data = json.loads(file.read())

a = 0

for person in data:
    if data[a]['gender'] == 'female':
        sw_women.writelines(data[a]['name'])
        sw_women.writelines("\n")
    elif data[a]['gender'] == 'male':
        sw_men.writelines(data[a]['name'])
        sw_men.writelines("\n")
    a += 1

file.close()
sw_women.close()
sw_men.close()