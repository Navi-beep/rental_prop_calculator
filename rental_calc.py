
go = True

class ROI:
    #create initialize function
    def __init__(self):
        self.cash_list = []


    #define a function for income
        #ask input for rental income
        #ask input for landry income
        #ask input for storage income
        #ask input for misc income
    #total all of the income for total monthly income
    
    def income(self):
        
        self.rental = int(input("What is your rental income? "))
        self.laundry = int(input("What is your laundry income? "))
        self.storage = int(input("What is your storage income? "))
        self.misc = int(input("What is your misc income? "))

        self.total_income = self.rental + self.laundry + self.storage + self.misc
        self.cash_list.append(self.total_income)
        return(f"Total Income : {self.total_income} ")
        

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
 
    def expenses(self):
        self.tax = int(input("What are your tax expenses? "))
        self.insurance = int(input("What are your insurance expenses? "))
        self.water_sewer = int(input("What are your water/sewer expenses? "))
        self.electric_gas = int(input("What are your electric/gas expenses? "))
        self.misc = int(input("What are your misc expenses? "))
        

        self.total_monthly_expenses = self.tax + self.insurance + self.water_sewer + self.electric_gas + self.misc 
        self.cash_list.append(self.total_monthly_expenses)
        return(f"Total Monthly Expenses: ${self.total_monthly_expenses} ")
        

        #define a function for cash flow
        #total monthly income - total monthly expenses
        # = total monthly cashflow
        #total monthly cashflow x 12 = total annual cash flow

    def cash_flow(self):

        self.total_monthly_cash_flow = ROI()

        self.total_monthly_cash_flow = self.total_income - self.total_monthly_expenses

        self.total_annual_cash_flow = self.total_monthly_cash_flow * 12 
        self.cash_list.append(self.total_annual_cash_flow)
        return(f"Total Annual Cash Flow: ${self.total_annual_cash_flow}") 
        


    #define a function for cash on cash return
    #ask for input for down payment
    #ask for input for closing costs
    #ask for input for rehab budget
    #ask for input for misc other
    #total of all the above to get Total Investment

    def cash_return(self):
        self.down_payment = int(input("What is your down payment?"))
        self.closing = int(input("What are your closing costs?"))
        self.rehab = int(input("What is your rehab budget? "))
        self.misc_expense = int(input("What are your misc expenses?"))

        self.total_investment = self.down_payment + self.closing + self.rehab + self.misc_expense 

        self.cash_on_cash_return = (self.total_annual_cash_flow / self.total_investment) * 100

        self.cash_list.append(self.cash_on_cash_return)

        return(f" Your cash on cash ROI is:  {self.cash_on_cash_return}")
        


    #calculate 
    #annual cash flow / total investment = X
    #take X * 100 to get cash on cash return!

    #print cash on cash return result

def run_ROI():
    my_ROI = ROI()
    while True:
        choose = input("Would you like to start analizing your cash on cash return? Press 'y' or 'n'. ")

        while choose not in {'y', 'n'}:
            choose = input("Please choose what you want to do! Please select 'y' or 'n'")
        if choose == 'y':
            my_ROI.income()
            my_ROI.expenses()
            my_ROI.cash_flow()
            my_ROI.cash_return()

        elif choose == 'n':
            break

run_ROI()
