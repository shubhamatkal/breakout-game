from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from lives import Lives
from levels import Level
from ball import Ball
import time

LEVEL = 1

scoreboard = Scoreboard()
pad = Paddle(0, -250)
ball = Ball()
lives = Lives()
level = Level()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Break Out")
screen.tracer(0)

screen.listen()
screen.onkey(pad.move_left, "Left")
screen.onkey(pad.move_right, "Right")

game_is_on = True
level.load_panels(LEVEL)
while game_is_on:

    screen.update()






screen.exitonclick()