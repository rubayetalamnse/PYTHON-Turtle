import turtle
from turtle import Turtle
from turtle import Screen

wn = Screen()

ruba = Turtle("turtle")
ruba.speed(0) #fastest possible speed

def dragging(x,y): #These parameters will be the mouse position
    ruba.ondrag(None) #a function with which will be called with the coordinates of the clicked point on the canvas
    ruba.setheading(ruba.towards(x,y)) #Return the angle between the line from turtle initial position to position specified by (x,y). 
    ruba.goto(x,y) 
    ruba.ondrag(dragging)

def clickRight(x,y):
    ruba.clear()

def main():  #this will run the program
    turtle.listen()
    ruba.ondrag(dragging)
    turtle.onscreenclick(clickRight,3)

    wn.mainloop() #until we close the turtle window, main function will keep working

main()


