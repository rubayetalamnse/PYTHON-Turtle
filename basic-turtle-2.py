import turtle

#create a turtle named ruba
ruba = turtle.Turtle()
ruba.speed(1)

#pencolor and pensize
ruba.pencolor("blue") #the line color is blue
ruba.pensize(10) #the line width is 10 pixels
ruba.right(90) #turtle will go downward
ruba.fd(100) #turtle will move 100 pixel downward


#initial a screen:
win = turtle.getscreen()

#background color and picture
win.bgcolor("red")
win.bgpic("D:\CODES FOR CERN\PYTHON PROJECTS\PYTHON turtle\python-bgpic-turtle.gif")
#the program and the gif file must be in the same directory

#where's the turtle--->
position = ruba.pos()
print ("position")
ruba.fd(100) 
ruba.lt(90)
ruba.fd(100)
ruba.pos()

#turtle window's size:
win.setup(800,600) #height = 800 pixels, width = 600 pixels
win.width = 1000
win.height = 500
win.title("My Project")
#win.clear()




turtle.hideturtle()
turtle.exitonclick()
ruba.done()