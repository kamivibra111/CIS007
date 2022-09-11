#Ex 2.13
#Muhammad Kamran Khan
#Date: 9/10/2022
#(Split digits) Write a program that prompts the user to enter a four-digit integer and print it reverse order.
#Muhammad Kamran Khan
#Date: 9/10/2022
num = eval(input("Enter a four-digit integer: "))
n1 = num % 10
num //= 10
n2 = num % 10
num //= 10
n3 = num % 10
num //= 10
n4 = num
print(n4)
print(n3)
print(n2)
print(n1)
