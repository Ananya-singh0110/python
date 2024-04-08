from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen=Screen()
screen.setup(800,600)
screen.title("Pong Game")
screen.bgcolor("Black")
screen.tracer(n=0)

paddle=Paddle()
paddle_2=Paddle()
paddle_2.goto(-340,0)

ball=Ball()
score=Scoreboard()






screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")
screen.onkey(paddle_2.go_up, key="w")
screen.onkey(paddle_2.go_down,key="s")

game_on= True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor()> 280 or ball.ycor()<-280:
       ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.xcor()> 320:
        ball.bounce_x()
        score.inc_score_r()
    if ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        score.inc_score_l()

    if ball.distance(paddle) >50 and ball.xcor() > 350:
        ball.goto(x=0,y=0)
        ball.bounce_x()
        ball.bounce_y()
        score.inc_score_l()
    if ball.distance(paddle_2) > 50 and ball.xcor() < -350:
        ball.goto(x=0, y=0)
        ball.bounce_x()
        ball.bounce_y()
        score.inc_score_r()
















screen.exitonclick()










