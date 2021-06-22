#simple python program to draw Bangladeshi Flag via turtle.

import turtle
from turtle import *

turtle.speed(0)
turtle.setup(1000,600)
turtle.bgcolor("green")

turtle.penup()
goto(-100,-100)
turtle.pendown()

turtle.color("red")
turtle.begin_fill()
turtle.circle(120)
turtle.end_fill()

turtle.hideturtle()
turtle.done()
turtle.exitonclick()
