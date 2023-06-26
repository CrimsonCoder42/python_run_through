import turtle
from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color : ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
START_POINT = 120


turtles = []


def make_turtle(color, y_axis):
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-225, y=y_axis)
    return turtle


for _ in range(0, len(colors)):
    turtles.append(make_turtle(colors[_], START_POINT - (40 * _)))

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            is_race_on = False
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner! ")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
