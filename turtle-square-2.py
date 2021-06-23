import turtle
from turtle import *
import random

#make a screen
win = turtle.Screen()
win.bgcolor("black")
win.setup(800,600)


#make a turtle
ruba = turtle.Turtle()
ruba.color("yellow")
ruba.shapesize(2,2)
ruba.speed(0)


#color list for the square:
color_list = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray", "white"]

#distance between each square
x = 10

#the loop!
#while True: #using while true it becomes an infinite loop! The squares keep printing out!
for i in range(50):
    random.shuffle(color_list)
    ruba.color(color_list[0])
    ruba.lt(90)
    ruba.fd(x)
    x += 10

turtle.exitonclick()
win.mainloop()
#in this program we have used total 20 colors, by random module, previously we could use only 6
