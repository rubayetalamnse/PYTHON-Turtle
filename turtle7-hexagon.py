#simple turtle program to generate a star
import turtle
from turtle import *

hexa = turtle.Turtle()

for i in range(6): #there is six side/arm of a hexagon
    hexa.forward(100) #length of each arm is 100 pixels
    hexa.right(60) #each arm is 60 degrees to the right

turtle.done()