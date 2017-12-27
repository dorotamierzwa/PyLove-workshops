file = open("file1.txt")
file = file.readlines()

eyes_height = {}

for person in file:

    eye_color = person[person.rfind("has ") + 4: person.find(" and")]
    height = int(person[person.rfind("is ") + 3: person.find(" cm")])

    if eye_color in eyes_height:
        eyes_height[eye_color].append(height)
    else:
        eyes_height[eye_color] = [height]


for eye_color in eyes_height:
    avg = sum(eyes_height[eye_color])/len(eyes_height[eye_color])

    print("Średni wzrost osób z kolorem oczu", eye_color, "wynosi", avg)

print(eyes_height)
