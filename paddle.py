from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_cor, y_cor)
        self.speed("fastest")

    def move_up(self):
        self.sety(self.ycor() + 30)

    def move_down(self):
        self.sety(self.ycor() - 30)






