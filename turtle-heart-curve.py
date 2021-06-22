import turtle
from turtle import *

turtle.bgcolor("cyan")
turtle.pensize(2)
turtle.color("red","pink")
turtle.speed(0)

def heart_curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
heart_curve() #first time we called the function for half of the heart
turtle.left(120)
heart_curve() #second time we called the function for another half of the heart
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()

turtle.done()
turtle.exitonclick()
