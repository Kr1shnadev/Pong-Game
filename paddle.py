from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.create_paddle(x, y)

    def create_paddle(self, x, y):
        self.shape("square")
        self.color("white")
        self.penup()
        self.left(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x, y)
        self.speed(0)

    def move_up(self):
        if self.ycor() > 230:
            pass
        else:
            self.forward(30)

    def move_down(self):
        if self.ycor() < -230:
            pass
        else:
            self.backward(30)
