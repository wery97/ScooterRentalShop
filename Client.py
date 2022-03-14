import random


class Client:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.id = self.surname[0] + self.name[0] + str(random.randint(1, 100))
        self.number_of_rents = 0
        self.percent_discount = 0

    def add_rent(self):
        self.number_of_rents += 1

    def check_discount(self):
        if self.number_of_rents == 0:
            self.percent_discount = 0
        elif 50 < self.number_of_rents < 100:
            self.percent_discount = 10
        elif 100 >= self.number_of_rents < 200:
            self.percent_discount = 25
        else:
            self.percent_discount = 50
