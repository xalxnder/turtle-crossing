import turtle
from turtle_crossing_classes import *
import time
TURTLE_START_POS = (0, -270)
INIT_CAR_SPEED = 10
turtle.colormode(255)

#Screen
screen = Screen()
screen.tracer(0)
screen.setup(700, 600)

#Create The Turtle
my_turtle = MainTurtle()

#Create The Level Text
level_text = Scoreboard(level=1)

#Control The Turtle
screen.listen()
screen.onkey(my_turtle.up, "Up")

#Generate the initial set of cars/blocks
for i in range(20):
	cars = Cars()

game_on = True

while game_on:
	if cars.car_list[-1].xcor() < 0:
		for car in cars.car_list:
			car.clear()
		cars = Cars()
	screen.update()
	# Check For Collision
	for car in cars.car_list:
		if my_turtle.distance(car) < 30:
			game_on = False
		cars.car_move(car)
	#Check if Turtle made it to next level
	if my_turtle.ycor() >= 270:
		level_text.level += 1
		print(level_text.level)
		my_turtle.setposition(TURTLE_START_POS)
		level_text.clear()
		level_text.setpos(-280, 260)
		level_text.write(f"Level: {level_text.level}", True, align="center", font=("Arial", 30, "normal"))
		cars.car_speed()
	time.sleep(0.1)

screen.exitonclick()
