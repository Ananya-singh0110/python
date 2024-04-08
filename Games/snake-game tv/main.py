import turtle
import snake
import time
from scoreboard import Score
from food import Food
screen=turtle.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(n=0)


snake=snake.Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on=True

while game_on:
    screen.update()
    time.sleep(.1)

    snake.move()
    if snake.segments[0].distance(food) < 15:
       food.refresh()
       snake.extend()
       score.inc_score()
    if snake.collide()==False:
        score.reset()
    for segment in snake.segments[1:]:
      if snake.segments[0].distance(segment)< 10:
            score.reset()
            snake.reset()













screen.exitonclick()














