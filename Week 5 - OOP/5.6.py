#to_burn - obliczyć ile czasu musi wykonywać jakąś czynność (bieganie to było 500 kcal/godzina),
#  żeby schudnąć do prawidłowej wagi, zakładając że jeden kilogram to 6000 kcal

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
        self.count_bmi()
        if self.bmi >= 25:
            kg_to_burn = self.weight - (25 * self.height ** 2)
            cal_to_burn = kg_to_burn * 6000
            running = cal_to_burn/500
            biking = cal_to_burn/600
            hobby = cal_to_burn/250
            chess = cal_to_burn/150
            print("Potrzebujesz {} godzin biegania, {} godzin jazdy na rowerze, {} godzin uprawiania hobby lub {} "
                  "godzin gry w szachy, by schudnąć {} kilogramów.".format(running, biking, hobby, chess, kg_to_burn))

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
Janusz.to_burn()
