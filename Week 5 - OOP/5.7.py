# - to_eat - obliczyć ile musi zjeść (ja wykorzystałam czekoladę - 450kcal porcja ) zakładając że jeden kilogram to 6000 kcal

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
            print("Powinieneś przytyć co najmniej", round((new_weight - self.weight), 2), "kg.")

        elif self.bmi >= 25:
            new_weight = 25 * self.height ** 2
            print("Powinieneś schudnąć co najmniej", round((self.weight - new_weight), 2), "kg.")

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
            print("Potrzebujesz {} godzin biegania, by schudnąć {} kilogramów.".format(running, kg_to_burn))

    def to_eat(self):
        self.count_bmi()
        if self.bmi < 18.5:
            kg_to_gain = (18.5 * self.height ** 2) - self.weight
            cal_to_gain = kg_to_gain * 6000
            chocolate = (cal_to_gain / 450)/100
            potato = (cal_to_gain / 80)/100
            print("Potrzebujesz zjeść {} kilogramów czekolady lub {} kilogramów ziemniaków, "
                  " by przytyć {} kilogramów.".format(chocolate, potato, round(kg_to_gain, 2)))

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

Janusz = Czlowiek("Janusz", 150, 1.80)
Janusz.to_eat()
