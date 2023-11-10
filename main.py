from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

screen.listen()
l_paddle = Paddle(x_cor=-350, y_cor=0)
r_paddle = Paddle(x_cor=350, y_cor=0)
ball = Ball()
score = Scoreboard()
game_on = True


# Movement of paddles controlled by the users
screen.onkeypress(key='w', fun=l_paddle.move_up)
screen.onkeypress(key='s', fun=l_paddle.move_down)
screen.onkeypress(key='Up', fun=r_paddle.move_up)
screen.onkeypress(key='Down', fun=r_paddle.move_down)

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    # The ball move for every fresh of the screen i.e.,
    # Here, 1) screen gets updated, 2) a delay of 0.1 second 3) then after 0.1 second, ball moves
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_off_wall()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_off_right_paddle()
        # print(f" post of right {ball.position()}")
        # print(f" dist of right {ball.distance(r_paddle)}")
        # print(ball.x_move)
        print(ball.move_speed)
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_off_left_paddle()
        print(ball.move_speed)


    # If ball pass the right person than left gets a point
    if ball.xcor() > 380:
        ball.reset()
        score.left_point()

    # If ball pass the left  person than right gets a point
    if ball.xcor() < - 380:
        ball.reset()
        score.right_point()
















screen.exitonclick()