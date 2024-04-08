import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S. State Game")
image="blank_states_img.gif"
screen.bgpic(image)
data=pandas.read_csv("50_states.csv")
state=data.state.to_list()
guessed_states=[]
while len(guessed_states)<50:
    answer = screen.textinput(title=f"{len(guessed_states)} / {50} states guessed", prompt="Guess the state name").title()
    if answer in state:
        guessed_states.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        sumn=data[data.state==answer]
        t.goto(x=int(sumn["x"]),y=int(sumn["y"]))
        t.write(answer)












def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

