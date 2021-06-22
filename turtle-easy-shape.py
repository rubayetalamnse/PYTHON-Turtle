import turtle
from turtle import *

turtle.penup()   #we don't want to see the lines
turtle.bgcolor("black") #the window background is black
turtle.speed(0) #fastes speed for drawing
turtle.shape("triangle") 
color_list = ["white","red","blue","green","yellow","cyan"] #we will see 6 different colors
#turtle.color("red") ----->#we will see only red color
for i in range(40,-1,-1):
    turtle.stamp()
    turtle.left(i)
    turtle.forward(20)
    turtle.color(color_list[i%6])
turtle.done()
turtle.exitonclick()