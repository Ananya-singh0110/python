import turtle
import random
screen=turtle.Screen()
screen.setup(500,400)
bet=screen.textinput("Make a bet!", "Which turtle will win the race? ")
y=[-90,-40,10,60,110,160]
colours=["red","blue","yellow","orange","purple","green"]
all_turt=[]
is_race_on=False

for turtle_index in range(0,6):
    timmy=turtle.Turtle(shape="turtle")
    timmy.color(colours[turtle_index])
    timmy.penup()
    timmy.goto(x=-230,y=y[turtle_index])
    all_turt.append(timmy)

if bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turt:
        if turtle.xcor() > 230:
            is_race_on=False
            winning_colour=turtle.pencolor()
            if winning_colour==bet:
                print("You won. Yay!")
            else:
                print(f"Sorry. You lost. Winning turtle was {winning_colour}")
        dist=random.randint(0,10)
        turtle.forward(dist)


















screen.exitonclick()

