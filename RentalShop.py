from Scooter import Scooter
import pickle


class RentalShop:
    def __init__(self, **stock):
        self.stock = stock
        self.list_of_scooters = []
        self.list_of_available_scooters = []
        self.list_of_rented_scooters = []
        self.available_small_scooters = 0
        self.available_big_scooters = 0
        self.given_password = ""
        self.correct_password = "pass"
        self.logged = False

        for key, value in stock.items():
            if key == "small_Scooter":
                for every in range(value):
                    self.list_of_scooters.append(Scooter(False, "Small Scooter {}".format(every+1)))
            else:
                for every in range(value):
                    self.list_of_scooters.append(Scooter(True, "Big Scooter {}".format(every+1)))

    def show_stock(self):
        print("In our offer we have:")
        j = 1
        for i in self.list_of_scooters:
            print(str(j) + "." + i.name)
            j += 1

    def show_available_scooters(self):
        print("Available scooters:")
        j = 0
        for i in self.list_of_scooters:
            if not i.busy:
                self.list_of_available_scooters.insert(j, i)
                print(str(j+1) + "." + i.name)
                j += 1
        if j == 0 and len(self.list_of_available_scooters) > 0:
            self.list_of_available_scooters.pop(0)
        else:
            for i in range(len(self.list_of_available_scooters) - j):
                self.list_of_available_scooters.pop()
        print("jest ich" + str(len(self.list_of_available_scooters)))

    def show_rented_scooter(self):
        print("Rented scooters:")
        j = 0
        for i in self.list_of_scooters:
            if i.busy:
                self.list_of_rented_scooters.insert(j, i)
                print(str(j+1) + "." + i.name)
                j += 1
        if j == 0 and len(self.list_of_rented_scooters) > 0:
            self.list_of_rented_scooters.pop(0)
        else:
            for k in range(len(self.list_of_rented_scooters) - j):
                self.list_of_rented_scooters.pop()
        print("jest ich" + str(len(self.list_of_rented_scooters)))

    def bill(self, scooter):
        return (scooter.return_scooter())*20

    def save_list_of_scooters(self, file):
        with open(file, 'wb') as fs:
            pickle.dump(self.list_of_scooters, fs)

    def upload_list_of_scooters(self, file):
        with open(file, 'rb') as fr:
            lista = pickle.load(fr)
        return lista

    def add_scooter(self, type_of_scooter, name):
        self.list_of_scooters.append(Scooter(type_of_scooter, name))

    def logging_owner(self):
        self.logged = False
        self.given_password = input("Type password")
        if self.given_password == self.correct_password:
            print("password correct\n")
            self.logged = True
        else:
            print("Password incorrect")
