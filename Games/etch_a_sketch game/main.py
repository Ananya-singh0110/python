import turtle
timmy=turtle.Turtle()
screen=turtle.Screen()
print(screen.canvheight)



def go_forward():
    timmy.forward(10)

def go_backward():
    timmy.back(10)

def go_clock():
    timmy.right(10)

def go_countclock():
    timmy.left(10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()



screen.listen()
screen.onkey(key="w", fun=go_forward)
screen.onkey(key="s", fun=go_backward)
screen.onkey(key="d", fun=go_clock)
screen.onkey(key="a", fun=go_countclock)
screen.onkey(key="c", fun=clear)












screen.exitonclick()
