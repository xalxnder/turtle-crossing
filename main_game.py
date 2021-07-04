import turtle
from turtle import Screen, Turtle
import time
#Screen
screen = Screen()
screen.tracer(0)

#Create The Turtle
turtle = Turtle()
turtle.penup()
turtle.shape("turtle")
turtle.setheading(90)


#Create The Blocks/Cars
car = Turtle()
car.penup()
car.shape("square")
car.shapesize(0.8, 4)
car.setpos(200,100)
car.setheading(180)

def car_move():
	car.forward(5)

#Control The Turtle
def up():
	turtle.forward(10)
screen.listen()
screen.onkey(up, "Up")


game_on = True

while game_on:
	screen.update()
	car_move()
	time.sleep(0.1)

screen.exitonclick()