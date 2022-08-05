
go = True

class ROI:
    #create initialize function
    def __init__(self, value):
        self.value = value
    
    def income(self):
        ask_1 = int(input("What is your rental income?"))
        ask_2 = int(input("What is your laundry income?"))
        ask_3 = int(input("What is your storage income?"))
        ask_4 = int(input("What is your misc income?"))

        total_income = ask_1 + ask_2 + ask_3 + ask_4
        print(total_income)

    
    def expenses(self):
        ask_5 = int(input("What is your tax expenses?"))
        ask_6 = int(input("What is your insurance expenses?"))
        ask_7 = int(input("What are your water/sewer expenses?"))
        ask_8 = int(input("What are your electric/gas expenses?"))
        ask_9 = int(input("What are your misc expenses?"))
        

        total_monthly_expenses = ask_5 + ask_6 + ask_7 + ask_8 + ask_9
        print(total_monthly_expenses)

    def cash_flow(self):

        total_monthly_cash_flow = ROI()

        total_monthly_cash_flow = total_income - total_monthly_expenses

        total_annual_cash_flow = total_monthly_cash_flow * 12 
        print(total_annual_cash_flow)


    def cash_return(self):
        ask_10 = int(input("What is your down payment?"))
        ask_11 = int(input("What are your closing costs?"))
        ask_12 = int(input("What is your rehab budget? "))
        ask_13 = int(input("What are your misc expenses?"))

        total_investment = ask_10 + ask_11 + ask_12 + ask_13

        cash_on_cash_return = (total_annual_cash_flow / total_investment) * 100

        print(cash_on_cash_return)




















    #define a function for income
        #ask input for rental income
        #ask input for landry income
        #ask input for storage income
        #ask input for misc income
    #total all of the income for total monthly income

    #define a function for expenses
     #ask for input for: taxes
     #ask for input for: insurance
     #ask for input for: water and sewer
     #ask for input for garbage
     #ask for input for electric/gas
     #ask for input for: HOA fees
     #ask for input for: lawn/snow
     #ask for input for: vacancy
     #ask for input for repairs
     #ask for input for capex
     #ask for input for: prop managment
     #ask for input for: mortgage
    #total of all inputs for total monthly expenses

    #define a function for cash flow
    #total monthly income - total monthly expenses
    # = total monthly cashflow
    #total monthly cashflow x 12 = total annual cash flow

    #define a function for cash on cash return
    #ask for input for down payment
    #ask for input for closing costs
    #ask for input for rehab budget
    #ask for input for misc other
    #total of all the above to get Total Investment

    #calculate 
    #annual cash flow / total investment = X
    #take X * 100 to get cash on cash return!

    #print cash on cash return result
    