#Ex 2.19
#Muhammad kamran khan
#Financial application: calculate future investment value)
#Date: 9/9/2022

amount = eval(input("Enter Investment Amount: "))
rate = eval(input("Enter Annual interest rate: ")) / (100 * 12)
years = eval(input("Enter number of years: ")) * 12

print("Accumulated value is: ", amount * (1 + rate) ** years)


