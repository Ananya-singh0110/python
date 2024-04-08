
SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
RIGHT=0
LEFT=180
DOWN=270
import turtle
class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        for position in SNAKE_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        snake = turtle.Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.segments[0].forward(MOVE_DISTANCE)
        self.collide()

    def up(self):
        if self.segments[0].heading() !=DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def collide(self):
        if self.segments[0].xcor()> 280 or self.segments[0].xcor()<-280 or self.segments[0].ycor()> 280 or self.segments[0].ycor()<-280:
            return False

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]





