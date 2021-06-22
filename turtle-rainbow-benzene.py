import turtle
color_list = ["white","red","blue","green","yellow","cyan"]
#t = turtle.Turtle()
t = turtle.Pen()
turtle.bgcolor("black")
for i in range(360):
    t.pencolor(color_list[i%6])
    t.width(i/1000+1)
    t.forward(i)
    t.left(59)

turtle.open()
