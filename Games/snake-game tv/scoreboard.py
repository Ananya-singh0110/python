from turtle import Turtle
from snake import Snake

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(0, 270)
        self.penup()
        self.highest=0
        self.color("White")
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score : {self.highest}" , align="center", font=("Ariel", 14, "normal"))
    def inc_score(self):
        self.score+=1
        self.update()

    def reset(self):
        if self.score>=self.highest:
            self.highest=self.score
        self.score=0
        self.update()


