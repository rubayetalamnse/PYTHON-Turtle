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

ruba.pendown()
ruba.pensize(10)
ruba.pencolor("white")
ruba.forward(200)


#clone our first turtle
chitti = ruba.clone()
chitti.left(120)
chitti.forward(200)
chitti.shape("turtle")

#another turtle :goku
goku = ruba.clone()
goku.shape("triangle")
goku.rt(120)
goku.forward(200)
goku.circle(100)

chitti.reset() #chitti comes to  (0,0)...at normal shape and normal color
chitti.dot(60)  #chitti turtle made a dot of 60 pixel radius
chitti.goto(280,-240) #chitti went to these coordinates by making a single black line

win.resetscreen() #chitti, ruba, and goku are now at (0,0),at normal shape and normal color
win.clearscreen() #we see a big white blank turtle window!
turtle.exitonclick()

