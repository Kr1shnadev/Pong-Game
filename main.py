import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PING PONG")
screen.tracer(0)
mid_line = Turtle()
mid_line.penup()
mid_line.speed(0)
mid_line.color("white")
mid_line.goto(0, 300)
mid_line.pendown()
mid_line.goto(0, -300)
scoreboard = ScoreBoard()
right_paddle = Paddle(x=350, y=0)
left_paddle = Paddle(x=-350, y=0)
ball = Ball()
screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.fast)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    if ball.xcor() < -400:
        ball.reset()
        scoreboard.r_point()
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.l_point()
screen.exitonclick()
