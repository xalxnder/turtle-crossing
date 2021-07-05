from turtle import Screen, Turtle
from random import  randint
import time
#Screen
screen = Screen()
screen.tracer(0)
screen.setup(700,600)

#Create The Turtle
my_turtle = Turtle()
my_turtle.penup()
my_turtle.shape("turtle")
my_turtle.setheading(90)
my_turtle.setposition(0,-200)

car_list = []

#Create The Blocks/Cars
num = 5
for i in range(10):
	car = Turtle()
	car.penup()
	car.shape("square")
	car.shapesize(0.8, 2)
	car.setpos(randint(0,200), randint(0,100))
	car.setheading(180)
	car_list.append(car)
print(car_list)


def car_move(car):
	car.forward(8)

#Control The Turtle
def up():
	my_turtle.forward(10)
screen.listen()
screen.onkey(up, "Up")


game_on = True

while game_on:
	screen.update()
	for car in car_list:
		car_move(car)
	time.sleep(0.1)

screen.exitonclick()