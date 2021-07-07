from turtle import Turtle, Screen
from random import randint

TURTLE_START_POS = (0, -270)
INIT_CAR_SPEED = 10


class MainTurtle(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.shape("turtle")
		self.setheading(90)
		self.setpos(TURTLE_START_POS)

	def up(self):
		self.forward(10)


class Cars(Turtle):
	car_list = []

	def __init__(self):
		super().__init__()
		self.penup()
		self.shape("square")
		self.shapesize(0.8, 2)
		self.setpos(randint(350, 800), randint(-500, 500))
		self.setheading(180)
		self.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
		self.car_list.append(self)

	def car_move(self, car):
		car.forward(INIT_CAR_SPEED)

	def car_speed(self):
		for car in self.car_list:
			car.forward(INIT_CAR_SPEED + 20)

class Scoreboard(Turtle):
	def __init__(self,level):
		self.level = level
		super().__init__()
		self.penup()
		self.hideturtle()
		self.setpos(-280, 260)
		self.write(f"Level: {self.level}", True, align="center", font=("Arial", 30, "normal"))



