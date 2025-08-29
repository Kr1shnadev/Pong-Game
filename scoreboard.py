from turtle import Turtle

ALIGNMENT = 'center'
FONT = "courier"
FONT_SIZE = "80"
TYPE = "normal"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_points()

    def update_points(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=(FONT, FONT_SIZE, TYPE))
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=(FONT, FONT_SIZE, TYPE))

    def r_point(self):
        self.r_score += 1
        self.update_points()

    def l_point(self):
        self.l_score += 1
        self.update_points()
