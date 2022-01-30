from RentalShop import RentalShop
from os.path import exists
shop_number_one = RentalShop(small_Scooter=5, big_Scooter=5)

fare = 0

if exists("scooter"):
    print("File exists")
    shop_number_one.list_of_scooters = shop_number_one.upload_list_of_scooters("scooter")

while True:

    print("Good morning\n How can i help you?")
    print("1. Rent a scooter")
    print("2. Return a scooter")
    print("3. Goodbye")
    a = input()
    if int(a) == 1:
        shop_number_one.show_available_scooters()
        if len(shop_number_one.list_of_available_scooters) == 0:
            print("There is no scooter to rent, sorry")
            continue
        b = input("Which one would you like to rent?\n")
        for every in shop_number_one.list_of_scooters:
            if every.name == shop_number_one.list_of_available_scooters[int(b)-1].name:
                every.rent()
            shop_number_one.save_list_of_scooters("scooter")
        continue
    elif int(a) == 2:
        shop_number_one.show_rented_scooter()
        if len(shop_number_one.list_of_rented_scooters) == 0:
            print("There are no rented scooters\n")
            continue

        c = input("Which one are you returning?\n")
        for each in shop_number_one.list_of_scooters:
            if each.name == shop_number_one.list_of_rented_scooters[int(c)-1].name:
                each.return_scooter()
                fare = divmod(each.rent_time.total_seconds(), 3600)[0]
                if divmod(each.rent_time.total_seconds(), 3600)[1] > 0:
                    fare += 1
        shop_number_one.save_list_of_scooters("scooter")
        print("You pay " + str(fare * 20) + "$")
    else:
        exit()
