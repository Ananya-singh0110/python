from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update()

    def update(self):
        self.goto(-180, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(180, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def inc_score_l(self):
            self.l_score += 1
            self.clear()
            self.update()

    def inc_score_r(self):
        self.r_score += 1
        self.clear()
        self.update()



