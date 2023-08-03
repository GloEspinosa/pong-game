from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_p = Paddle((460, 0))
left_p = Paddle((-460, 0))
ball = Ball()
left_score = Scoreboard((-100, 250))
right_score = Scoreboard((100, 250))

screen.listen()
screen.onkey(right_p.up, "Up")
screen.onkey(right_p.down, "Down")
screen.onkey(left_p.up, "w")
screen.onkey(left_p.down, "s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(right_p) < 50 and ball.xcor() > 320 or ball.distance(left_p) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Tracking scores and reset ball when paddle misses
    if ball.xcor() == 500:
        left_score.increase_score()
        ball.reset_position()
    elif ball.xcor() == -500:
        right_score.increase_score()
        ball.reset_position()

    if left_score.score == 10 or right_score.score == 10:
        game_on = False


screen.exitonclick()
