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

    if key == "yellow":
        key = "żółty"
    elif key == "black":
        key = "czarny"
    elif key == "blue":
        key = "niebieski"
    elif key == "orange":
        key = "pomarańczowy"
    elif key == "green, yellow":
        key = "żółto-zielony"
    elif key == "red":
        key = "czerwony"
    elif key == "brown":
        key = "brązowy"
    elif key == "unknown":
        key = "nieznany"
    elif key == "gold":
        key = "złoty"
    elif key == "blue-gray":
        key = "szaro-niebieski"
    elif key == "pink":
        key = "różowy"
    elif key == "hazel":
        key = "orzechowy"
    elif key == "red, blue":
        key = "czerwono-niebieski"

    print("Średni wzrost osób z kolorem oczu", key, "wynosi", average_height)
    