from turtle import Screen
from paddle import Paddle
import time

pad = Paddle(0, -250)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Break Out")
screen.tracer(0)

screen.listen()
screen.onkey(pad.move_left, "a")
screen.onkey(pad.move_right, "d")

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.01)





screen.exitonclick()