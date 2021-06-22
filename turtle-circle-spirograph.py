import turtle

turtle.bgcolor("black") #background is made black
turtle.pensize(3) #pensize required for drawing circle shapes
color_list = ["white","red","blue","green","yellow","cyan"] #6 different color for 6 different circles
for i in range(6): #range(6) means---> 0,1,2,3,4,5--total 7 circle will be drawn by each color
    for colors in color_list:
        turtle.color(color_list[i])
        turtle.circle(100) #100 is circle radius
        turtle.right(10) #right----> circle will start popping up from left to right, 10 is circle to circle distance.
#turtle.left--->circle will start popping up from right to left
turtle.speed(0)
turtle.hideturtle()
turtle.open()
turtle.done()
#don't use more than 6 colors, if you use more colors than you won't be able to see all the colored circles
#turtle.open()---> the turtle window will not colse immediately