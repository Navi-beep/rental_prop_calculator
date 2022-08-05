def income():
        ask_1 = int(input("What is your rental income?"))
        ask_2 = int(input("What is your laundry income?"))
        ask_3 = int(input("What is your storage income?"))
        ask_4 = int(input("What is your misc income?"))

        total_income = ask_1 + ask_2 + ask_3 + ask_4

        print(total_income)

income()