from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def face_left():
    tim.left(10)


def face_right():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=face_left)
screen.onkey(key="d", fun=face_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()