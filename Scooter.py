import datetime


class Scooter:
    def __init__(self, type, name):
        self.type = type
        self.rent_date = 0
        self.return_date = 0
        self.busy = False
        self.name = name
        self.rent_time = 0

    def rent(self):
        self.rent_date = datetime.datetime.now()
        self.busy = True

    def return_scooter(self):
        self.return_date = datetime.datetime.now()
        self.busy = False
        self.rent_time = self.return_date - self.rent_date
