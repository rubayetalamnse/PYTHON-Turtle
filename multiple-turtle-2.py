import turtle
from turtle import *

#make a screen
win = turtle.Screen()
win.bgcolor("purple")
win.setup(800,600)


#make a turtle
ruba = turtle.Turtle()
ruba.shape("square")
ruba.color("yellow")
ruba.shapesize(5,5)
ruba.circle(100,180)

#clone our first turtle
chitti = ruba.clone()
chitti.left(120)
chitti.forward(200)
chitti.shape("turtle")
chitti.circle(100,270)

#another turtle :goku
goku = ruba.clone()
goku.shape("triangle")
goku.lt(90)
goku.forward(200)
goku.circle(100,90)

turtle.exitonclick()