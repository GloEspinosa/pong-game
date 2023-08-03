from turtle import Turtle

DISTANCE_MOVED = 30


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(position)

    def up(self):
        new_y = self.ycor() + DISTANCE_MOVED
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - DISTANCE_MOVED
        self.goto(self.xcor(), new_y)



