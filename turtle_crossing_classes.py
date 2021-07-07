from turtle import Turtle, Screen

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

