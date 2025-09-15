from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up,"Up" )
screen.onkey(r_paddle.down, "Down" )
screen.onkey(l_paddle.up, "w" )
screen.onkey(l_paddle.down,"s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()


    #Detect collision with paddle
    if r_paddle.distance(ball)<55 and ball.xcor()>330 or l_paddle.distance(ball)<55 and ball.xcor()<-330 :
        ball.bounce_x()


    if ball.xcor() > 370:
        score.clear()
        score.increase_score("l")
        ball.reset()

    if ball.xcor() < -370:
        score.clear()
        score.increase_score("r")
        ball.reset()

screen.exitonclick()
