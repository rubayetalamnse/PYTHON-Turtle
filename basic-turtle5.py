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


ruba.forward(100)
ruba.stamp() #wherever it stopped and moved a turtle will be seen
ruba.left(90)

ruba.forward(100)
ruba.stamp()
ruba.left(90)
ruba.backward(100)
ruba.stamp()
#ruba.undo()
#ruba.undo()
ruba.clearstamp(2)
ruba.clearstamps()

ruba.heading() #works in shell


turtle.exitonclick()
