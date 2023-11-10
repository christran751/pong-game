from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.reset_score()

    def reset_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f"{self.left_score}", move=False, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(arg=f"{self.right_score}", move=False, align='center', font=('Courier', 80, 'normal'))

    def left_point(self):
        self.left_score += 1
        self.reset_score()

    def right_point(self):
        self.right_score += 1
        self.reset_score()







