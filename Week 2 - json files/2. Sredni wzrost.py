# Zapisz średni wzrost postaci dla każdego z kolorów w osobnych linijkach w formie:
# Średni wzrost osób z kolorem oczu blue wynosi 123,12 cm.


file = open("file1.txt")
file = file.readlines()

eyes_height = {}

for person in file:

    eye_color = person[person.rfind("has ") + 4: person.find(" and")]
    height = int(person[person.rfind("is ") + 3: person.find(" cm")])

    if eyes_height.get(eye_color) is None:
        eyes_height[eye_color] = []

    eyes_height[eye_color].append(height)

for key in eyes_height:
    average_height = round(sum(eyes_height[key]) / len(eyes_height[key]), 2)
    print("Średni wzrost osób z kolorem oczu", key, "wynosi", average_height)
























