import turtle
from turtle import Screen, Turtle
from random import  randint
import time
TURTLE_START_POS = (0, -270)
INIT_CAR_SPEED = 10
level = 1

turtle.colormode(255)
#Screen
screen = Screen()
screen.tracer(0)
screen.setup(700,600)
# screen.screensize(700,700)

#Create The Turtle
my_turtle = Turtle()
my_turtle.penup()
my_turtle.shape("turtle")
my_turtle.setheading(90)
my_turtle.setposition(TURTLE_START_POS)

#Create The Level Text
level_text = Turtle()
level_text.penup()
level_text.hideturtle()
level_text.setpos(-280, 260)
level_text.write(f"Level: {level}", True, align="center", font=("Arial", 30, "normal"))

car_list = []

#Create The Blocks/Cars
def generate_cars():
	for i in range(20):
		car = Turtle()
		car.penup()
		car.shape("square")
		car.shapesize(0.8, 2)
		car.setpos(randint(350,800), randint(-500,500))
		car.setheading(180)
		car.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
		car_list.append(car)


def car_move(car):
	car.forward(INIT_CAR_SPEED)


def car_speed():
	for car in car_list:
		car.forward(INIT_CAR_SPEED + 20)


generate_cars()




#Control The Turtle
def up():
	my_turtle.forward(10)
	print(my_turtle.ycor())

screen.listen()
screen.onkey(up, "Up")


game_on = True

while game_on:
	if car_list[-1].xcor() < 0:
		for car in car_list:
			car.clear()
		generate_cars()
	screen.update()
	# Check For Collision
	for car in car_list:
		if my_turtle.distance(car) < 40:
			game_on = False
		car_move(car)
	#Check if Turtle made it to next level
	if my_turtle.ycor() >= 270:
		level += 1
		my_turtle.setposition(TURTLE_START_POS)
		level_text.clear()
		level_text.setpos(-280, 260)
		level_text.write(f"Level: {level}", True, align="center", font=("Arial", 30, "normal"))
		car_speed()
	time.sleep(0.1)

screen.exitonclick()