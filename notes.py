#print("'MURICA")

#for i in range(5):
#        i = ("*********----------------")
 #       print(i)
###for a in range(5):
 #       a = ("-------------------------")
#       print(a)


def expenses():
        ask_5 = int(input("What are your tax expenses?"))
        ask_6 = int(input("What are your insurance expenses?"))
        ask_7 = int(input("What are your water/sewer expenses?"))
        ask_8 = int(input("What are your electric/gas expenses?"))
        ask_9 = int(input("What are your misc expenses?"))
        

        total_monthly_expenses = ask_5 + ask_6 + ask_7 + ask_8 + ask_9
        print(total_monthly_expenses)

expenses()
