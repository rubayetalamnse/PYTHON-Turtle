#simple turtle program to generate a star
import turtle 
from turtle import *

star = turtle.Turtle()

for i in range(5): # there is 5 arm of a star
    star.forward(150)  #every arm will be 150 pixels
    star.right(144)  #the turtle will move at 144 degree to create the star

turtle.done()