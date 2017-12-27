file = open("file1.txt")
people = file.readlines()


file_plus = open("hero_200_plus.txt", "w")
file_short = open("hero_short.txt", "w")


for person in people:
    psplit = person.split(' ')
    height = int(psplit[-3])


    if height >= 200:
        file_plus.write(person)

    else:
        file_short.write(person)

file.close()
file_short.close()
file_plus.close()
