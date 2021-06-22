import turtle
import random

color_list = ["red", "green", "blue", "yellow", "purple", "cyan"]

#set colors for turtle------------>>>>
turtle.color("red", "green") #red color for the boundary, green color for inside shape
turtle.shape("turtle")
#set pen width------------------------
turtle.width(5) #boundary thickness 5 pixels

#fill shape with colors
turtle.begin_fill()
turtle.circle(50) #radius 50 pixels
turtle.end_fill()

#penup --pendown------------------------
turtle.penup() #now we can't see the line
turtle.forward(150)
turtle.pendown() 
turtle.color("yellow","blue") #turtle outside yellow, inside blue

#make a square with for loop in turtle and shape,fill is also used ---->
turtle.begin_fill()
for x in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
#the square boundary will be yellow and inside blue.

#now we will draw different circle with different colors and shape------>
for x in range(10): #10 random circles will be drawn
    randColor = random.randrange(0,len(color_list))
    turtle.color(color_list[randColor]) #here the boundary and the shape will be same color 
   #turtle.color(color_list[randColor], color_list[random.randrange(0,len(color_list))])---->here we will have different color in boundary and different color in inside of the shape
    rand1 = random.randrange(-300,300) # positive negative x coordinate (left,right)
    rand2 = random.randrange(-300,300) #positive negative x coordinate (up,down)
    turtle.penup()
    turtle.setpos((rand1,rand2)) # circle position
    turtle.pendown()
    turtle.begin_fill() #circle color fill
    turtle.circle((random.randrange(0,80))) #circle radius will be between 0 and 80 pixels
    turtle.end_fill()


turtle.exitonclick()