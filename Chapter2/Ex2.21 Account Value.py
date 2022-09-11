#Ex (2.21)
#Muhammad Kamran Khan
#(Financial application: compound value)
#Date: 9/10/2022

#asking user to input the monthly saving amount
MonthlySavingAmount = eval(input("Enter the monthly saving Amount: "))
interest_rate = 0.00417
#multiplying monthly saving input with interest rate and then adding 1 to it.
total = MonthlySavingAmount * (1 + interest_rate)

total = (MonthlySavingAmount + total) * (1 + interest_rate)
total = (MonthlySavingAmount + total) * (1 + interest_rate)
total = (MonthlySavingAmount + total) * (1 + interest_rate)
total = (MonthlySavingAmount + total) * (1 + interest_rate)
total = (MonthlySavingAmount + total) * (1 + interest_rate)
print("After Sixth month the account value is: ", total)
