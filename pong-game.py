# simple pong game by Python 3 using turtle
import turtle
import winsound #for bounce sounds

# pong = turtle.Turtle() #turtle name
turtle.title("Pong by @RubayetAlam13")  # turtle title doesn't work
turtle.bgcolor("black")
turtle.setup(width=800, height=600)  # turtle window's width and height
turtle.tracer(0)  # stops window from updating

#score:
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
# this is the speed of animation,this's just something that we need to do for turtle module.it sets the speed to maximum possible speed. It will draw everythin fast on the turtle window.
paddle_a.speed(0)
# there are also some other shapes: circle, square, triangle turtle, classic etc.
paddle_a.shape("square")
paddle_a.color("yellow")  # paddle color will be blue
# by default the shape size is 20px,20px; when we have used stretch_len =5---> means 5*20--->width becomes 100px, but the height remains same
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # we are not drawing anything here. So it's penup.
paddle_a.goto(-350, 0)


# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed("slowest")
ball.shape("square")
ball.color("yellow")
ball.speed(2)
#ball.shapesize(stretch_wid=5, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 2  # d = delta, changes the ball position, every time the ball moves, it moves by 2 pixels. x is positive and the ball moves to the right
ball.dy = 2  # since y is positive, the ball moves to the up

#pen for scoring
pen = turtle.Turtle()
pen.speed(1)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0 Player B:0",align="center",font = ("Courier",24,"normal"))

# function
def paddle_a_up():
    y = paddle_a.ycor()
    y = y+20  # when the paddle_a moves up, the y value increases
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y = y-20  # when the paddle_a moves down, the y value decreases
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y = y+20  # when the paddle_b moves down, the y value increases
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y = y-20  # when the paddle_a moves down, the y value decreases
    paddle_b.sety(y)


# keyboard binding
turtle.listen()  # turtle will move according the key we press
# whenever we press w button in the keyboard, it will call the "paddle_a_up" function, and will move upward by 20 pixels.
turtle.onkeypress(paddle_a_up, "w")
turtle.onkeypress(paddle_a_down, "s")
turtle.onkeypress(paddle_b_up, "Up")
turtle.onkeypress(paddle_b_down, "Down")

# main game loop---------------------------------------------->>>>>>>
while True:
    turtle.update()  # every time the loop runs, it updates the window

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # BORDER CHECKING-------------------------------->>>>>>>>>>>>>>>

    #border checking for y coordinates (top border)
    if ball.ycor() >290: #our window height is 600 pixels, so from (0,0), it's +300 upward and -300 downward, and our ball is 10 pixels, so its 290 pixels.
        ball.sety(290)
        ball.dy *= -1 #ball.dy = 2, now -2, it will reverse the direction of the ball. the ball will bounce on the upper boundary of the window.
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #border checking for y coordinates (bottom border)
    elif ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    #border checking for x coordinates ( border)
    if ball.xcor()>350: #our width of the window is 800 pixels, to the left 400, subtracting the balls width its 390
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear() #to remove the initial points ---> 0
        pen.write("Player A:{} Player B:{}".format(score_a,score_b),align="center",font = ("Courier",24,"normal")) #24 is fontsize, instead of normal we can use bold/italic

     #border checking for x coordinates ( border)
    elif ball.xcor()<-350:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a,score_b),align="center",font = ("Courier",24,"normal"))
        winsound.PlaySound("bounce2.wav", winsound.SND_ASYNC)
    #ball and paddle collision:
    if ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()<paddle_b.ycor()+50 and ball.ycor()> paddle_b.ycor()-50):
        ball.setx(340)
        ball.dx *= -1
    elif ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()<paddle_a.ycor()+50 and ball.ycor()> paddle_a.ycor()-50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce2.wav", winsound.SND_ASYNC)



# turtle.open()
# turtle.exitonclick()
