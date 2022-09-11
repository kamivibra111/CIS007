#Ex 2.5
#Kamran khan
#Tip Calculator
#date: 9/10/2022

#asking user to input the total billing amout before adding tip

subtotal = eval(input("Enter total bill amount: "))

#asking user for tip amount in percentage

tippercentage = eval(input("Enter the tip percentage: "))

#typing the tip formula

tip = subtotal*tippercentage/100
print("Tip amout is ", tip)

#Now adding total amout and tip all togather for a final total

print("Your total bill including tip is: ", tip + subtotal)
