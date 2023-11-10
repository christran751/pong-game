from turtle import Turtle
# ball fucks up at x 10 and y - 15
# random.choice([-15, -11, 11, 15])
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = -15
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_off_wall(self):
        self.y_move *= -1

    def bounce_off_left_paddle(self):
        self.x_move = abs(self.x_move)
        self.move_speed *= 0.9

    def bounce_off_right_paddle(self):
        self.x_move = - abs(self.x_move)
        # Here: The logic of – abs(self.x_move) return the negative version of whatever the absolute value of x_move is
        self.move_speed *= 0.9

    def reset(self):
        self.home()
        self.x_move *= - 1
        self.move_speed = 0.1





