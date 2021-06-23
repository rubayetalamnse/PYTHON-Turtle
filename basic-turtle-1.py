import turtle

#create a turtle named ruba
ruba = turtle.Turtle()

#lets check forward and penup, pendown functions
ruba.forward(50) #first turtle will draw a line of 50 pixel
ruba.penup() #now no lines will be drawn
ruba.forward(100) #without drawing lines turtle will move 100 pixels forward
ruba.pendown() #now we will see the turtle
ruba.clear() #clear whatever we drew 

#lets make a 120 degree triangle 
ruba.forward(100)
ruba.left(120) #right/left function can only take angle
ruba.forward(100)
ruba.clear() #clear function can't take us to the initial position

#what if we use right angle
ruba.forward(100)
ruba.right(120) #right/left function can only take angle
ruba.forward(100)

#
ruba.clear() 
ruba.penup()
ruba.home() #comes back to the initial position (0,0)
#ruba.shapesize(5,5) #stretch_wid =5, stretch_len = 5, border/outline =0
ruba.turtlesize(5,5) #same as shapesize
ruba.speed(1) #---->slowest speed
ruba.reset()

#different shapes:
ruba.shape("turtle")
ruba.fd(400)
ruba.shape("triangle")
ruba.lt(90)
ruba.fd(300)
ruba.shape("circle")
ruba.lt(90)
ruba.fd(400)
ruba.shape("classic")
ruba.lt(90)
ruba.fd(200)
ruba.shape("arrow")
ruba.clear()
ruba.reset()


turtle.exitonclick()
