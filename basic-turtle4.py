import turtle
from turtle import *

#make a screen
win = turtle.Screen()
win.bgcolor("purple")
win.setup(800,600)
win.title("Multiple Square")


#make a turtle
ruba = turtle.Turtle()
ruba.shape("turtle")
ruba.color("yellow")
ruba.pencolor("white")
#setx---> distance in x coordinates
ruba.setx(150)
#sety---> distance in y coordinates
ruba.sety(100)

ruba.home() #comes to (0,0)
ruba.reset()




win.mainloop()
turtle.exitonclick()


