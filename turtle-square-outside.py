import turtle
from turtle import *

wn = turtle.Screen()
wn.bgcolor("cyan")
wn.title("Spiral Square Outside In and Inside Out")

ruba = turtle.Turtle()
ruba.color("red") 

def Squarefunction(size):
    for i in range(4):
        ruba.forward(size)
        ruba.left(90)
        size = size+5 #the difference between each circle is 5 pixels

Squarefunction(146)
Squarefunction(126)
Squarefunction(106)
Squarefunction(86)
Squarefunction(66)
squarefunction(46)
squarefunction(26)


turtle.open()
turtle.exitonclick()
turtle.done()