# Zaimplementuj zapisywanie JSON z danymi danego "Człowieka" na dysk pod plikiem <imie>.json (save_data).
import json

class Czlowiek:
    bmi = 0

    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def speak(self):
        print("Mówię prawdę.")

    def count_bmi(self):
        bmi = self.weight/self.height**2
        print("Twoje BMI to", bmi)
        self.bmi = bmi
        return bmi

    def diff_to_norm(self):
        self.count_bmi()
        if self.bmi < 18.5:
            new_weight = 18.5 * self.height ** 2
            print("Powinieneś przytyć co najmniej", new_weight - self.weight, "kg.")

        elif self.bmi >= 25:
            new_weight = 25 * self.height ** 2
            print("Powinieneś schudnąć co najmniej", self.weight - new_weight, "kg.")

    def save_data(self):
        with open('{}.json'.format(self.name), 'w') as file:
            json.dump(
                {
                    'waga': self.weight,
                    'imie': self.name,
                    'wzrost': self.height
                },
                file
            )

    def to_burn(self):
        pass

    def to_eat(self):
        pass

    def what_to_do(self):
        pass

class Polityk(Czlowiek):
    bribed = False

    def speak(self):
        if self.bribed:
            super().speak()
        else:
            print("Kłamię, bo mogę.")

    def receive_bribe(self):
        self.bribed = True

Janusz = Czlowiek("Janusz", 50, 1.80)
Janusz.save_data()