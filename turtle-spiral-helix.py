import turtle
from turtle import *

wn = turtle.Screen()
wn.title("Spiral Helix by Rubayet")
wn.bgcolor("black")
color_list = ["white","red","blue","green","yellow","cyan"]
turtle.speed(2)
#turtle.color("red")
for i in range(50):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
    turtle.color(color_list[i%6])

turtle.exitonclick()
turtl.done()
