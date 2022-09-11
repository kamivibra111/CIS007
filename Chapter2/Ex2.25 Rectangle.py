#Ex 2.25
#Muhammad Kamran Khan
#Date: 9/10/2022


import turtle
centerX = eval(input("Enter CenterX: "))
centerY = eval(input("Enter CenterY: "))
w = eval(input("Enter the width: "))
h = eval(input("Enter the hight: "))

turtle.penup()
turtle.goto(centerX - 0.5 * w, centerY + 0.5 * h)
turtle.pendown()
turtle.forward(w)
turtle.right(90)
turtle.forward(h)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(h)

turtle.done()
