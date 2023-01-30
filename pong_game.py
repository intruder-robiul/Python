import turtle
import winsound

window = turtle.Screen()
window.title("Pong Game by Intruder")
window.bgcolor("White")
window.setup(width=1000, height=700)
window.tracer(0)

# Scores
score_a = 0
score_b = 0

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.penup()
paddle_a.goto(-460, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.penup()
paddle_b.goto(460,0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write("Player A: 0 Player B:0", align="center", font=("Courier", 14, "normal"))


#Function

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 340:
        ball.sety(340)
        ball.dy *= -1
        winsound.PlaySound("pong.mp3", winsound.SND_ASYNC)

    if ball.ycor() < -340:
        ball.sety(-340)
        ball.dy *= -1
        winsound.PlaySound("pong.mp3", winsound.SND_ASYNC)

    if ball.xcor() > 490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 14, "normal"))

    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 14, "normal"))

    if (ball.xcor() > 440 and ball.xcor() < 450) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(440)
        ball.dx *= -1
        winsound.PlaySound("ping.mp3", winsound.SND_ASYNC)

    if (ball.xcor() < -440 and ball.xcor() > -450) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-440)
        ball.dx *= -1
        winsound.PlaySound("ping.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)