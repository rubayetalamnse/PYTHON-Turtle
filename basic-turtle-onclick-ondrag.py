import turtle
from turtle import *

#make a screen
win = turtle.Screen()
win.bgcolor("black")
win.setup(800,600)


#make a turtle
ruba = turtle.Turtle()
ruba.color("yellow")
ruba.shapesize(2,2)
ruba.speed(0)

def make(x,y):
    for i in range(4):
        ruba.lt(90)
        ruba.fd(100)

win.onclick(make)

turtle.exitonclick()