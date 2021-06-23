import turtle
from turtle import *

#make a screen
win = turtle.Screen()
win.bgcolor("purple")
win.setup(800,600)


#make a turtle
ruba = turtle.Turtle()
ruba.color("yellow")
ruba.shapesize(2,2)

#make a square by setheading function
ruba.setheading(0)
ruba.fd(100)
ruba.setheading(90)
ruba.fd(100)
ruba.setheading(180)
ruba.fd(100)
ruba.setheading(270)
ruba.fd(100)

turtle.exitonclick()