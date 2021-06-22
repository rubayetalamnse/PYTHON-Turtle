import turtle
import random
from turtle import *

ruba = turtle.Turtle()
ruba.width(5)
ruba.speed(0)
color_list = ["purple","red","blue","green","yellow","cyan"]

#function to move our turtle

def up():
    ruba.setheading(90)
    ruba.forward(100)

def down():
    ruba.setheading(270)
    ruba.forward(100)

def left():
    ruba.setheading(180)
    ruba.forward(100)

def right():
    ruba.setheading(360)
    ruba.forward(100)

def clickLeft(x, y):
    ruba.color(random.choice(color_list))
def clickRight(x, y):
    ruba.color(random.choice(color_list))


turtle.listen()
turtle.onkey(up, "Up") #this automatically calls the up function to move turtle upward
turtle.onkey(down, "Down") #this automatically calls the up function to move turtle upward
turtle.onkey(left, "Left") #this automatically calls the up function to move turtle upward
turtle.onkey(right, "Right") #this automatically calls the up function to move turtle upward


#this is for mous left and right button, these button will change the color of the turtle
turtle.onscreenclick(clickLeft,1) #1=default mouse left button
turtle.onscreenclick(clickRight,3) #3=default mouse right button

turtle.mainloop()
