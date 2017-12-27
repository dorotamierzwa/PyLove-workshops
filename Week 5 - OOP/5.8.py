# czy ma schudnąć czy przytyć na podstawie wagi

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
        kg_to_burn = self.weight - (25 * self.height ** 2)
        cal_to_burn = kg_to_burn * 6000
        running = cal_to_burn/500
        print("Powinieneś schudnąć.")
        print("Potrzebujesz {} godzin biegania, by schudnąć {} kilogramów.".format(round(running, 2), round(kg_to_burn, 2)))

    def to_eat(self):
        kg_to_gain = (18.5 * self.height ** 2) - self.weight
        cal_to_gain = kg_to_gain * 6000
        chocolate = cal_to_gain / 450
        potato = (cal_to_gain / 80) / 100
        print("Powinieneś przytyć.")
        print("Potrzebujesz zjeść {} kilogramów czekolady lub {} kilogramów ziemniaków, "
              " by przytyć {} kilogramów.".format(round(chocolate, 2), round(potato, 2), round(kg_to_gain, 2)))

    def what_to_do(self):
        self.count_bmi()
        if self.bmi < 18.5:
            self.to_eat()
        elif self.bmi >= 25:
            self.to_burn()
        else:
            print("Twoja waga jest prawidłowa.")


class Polityk(Czlowiek):
    bribed = False

    def speak(self):
        if self.bribed:
            super().speak()
        else:
            print("Kłamię, bo mogę.")

    def receive_bribe(self):
        self.bribed = True

Janusz = Czlowiek("Janusz", 80, 1.80)
Janusz.what_to_do()
