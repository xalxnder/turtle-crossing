import turtle
from turtle import Screen
import time
#Create The Turtle
turtle = turtle.Turtle()
turtle.penup()
turtle.shape("turtle")
turtle.setheading(90)
screen = Screen()

#Control The Turtle
def up():
	turtle.forward(50)


screen.listen()
screen.onkey(up, "Up")




screen.exitonclick()