import turtle
from turtle_crossing import *
import time

TURTLE_START_POS = (0, -270)
INIT_CAR_SPEED = 10
turtle.colormode(255)

# Screen
screen = Screen()
screen.tracer(0)
screen.setup(700, 600)

# Create The Turtle
my_turtle = MainTurtle()

# Create The Level Text
level_info = Scoreboard(level=1)

# Control The Turtle
screen.listen()
screen.onkey(my_turtle.up, "Up")
screen.onkey(my_turtle.down, "Down")

# Generate the initial set of cars/blocks
for i in range(20):
    cars = Cars()


game_on = True

while game_on:
    if cars.car_list[-1].xcor() < 0:
        for car in cars.car_list:
            car.clear()
        for i in range(20):
            cars = Cars()
    # Check For Collision
    for car in cars.car_list:
        if my_turtle.distance(car) < 30:
            game_on = False
        cars.car_move(car)
    # Check if Turtle made it to next level
    if my_turtle.ycor() >= 270:
        level_info.reset(my_turtle)
        cars.car_speed()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
