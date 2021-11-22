#Finance Calulators
#Im importing the math library as there are math calculations in this task

import math

print("Choose either \'bond\' or \'investment\' from the menu below to proceed:")
print()
print("investment - to calculate the amount of interest you'll earn on interest")
print("bond - to calculate the amount you'll have to pay on a home loan")
print()

#I am using finance_type as my variable for the choice of each calculator
#I used .capitalize() at each instance of a user input so that every posssibility of typing each choice is a valid choice

finance_type=input("Enter choice: ").capitalize()
print()

#Below I am showing the calculations

#I used an 'and' statement for the specific length the word also needs to be in order further secure the input 

if finance_type == "Investment" and len(finance_type) == 10:

    #inv is short for investment
    inv_amount = float(input("Enter the amount to be invested: R")) #I inserted the R for the user to just insert the interger value 
    inv_int_rate = float(input("Enter the interest rate percentage value: "))/100 #I divided the input by 100 to get the decimal value to be consistent in the calculations
    inv_years = float(input("Enter the amount of years for investing: "))
    print()
    interest = input("Choose either \'simple\' or \'compound\' interest: ").capitalize()

    if interest == "Simple" and len(interest) == 6:
        #Below is the simple interest calculation using the input found by choosing investing
        simple_total = inv_amount*(1+inv_int_rate*inv_years) 
        print("Your simple interest total is R" + str(simple_total))

    elif interest == "Compound" and len(interest) == 8:

          #Below is the compound interest calculation using the input found by choosing 'investment'
          compound_total = round(inv_amount*math.pow((1+inv_int_rate),inv_years),2) #I round for the actual value to be paid
          print("Your compound interest total is R"+str(compound_total))


elif finance_type == "Bond" and len(finance_type) == 4:
    house_value = float(input("Enter the value of the house: R")) #I inserted the R for the user to just insert the interger value

    #Below i divide by 1200 to show the monthly decimal value we will need to be consistent in the calculation
    month_int_rate = float(input("Enter the monthly interest rate percentage value: "))/1200
    repay_months = float(input("Enter the number of months over which the bond will be paid: "))

    #Below is the bond repayment calcualtion using the input found by choosing 'bond
    bond_payments = round((month_int_rate*house_value)/(1-math.pow((1+month_int_rate),-repay_months)),2) #I round for the actual value to be paid
    print() 
    print("Your monthly bond repayments are R"+ str(bond_payments))

#This else statement serves to show that any other input other than the ones specified will cause an error in the calculation

else:
    print("Please enter a valid choice and start again.")
