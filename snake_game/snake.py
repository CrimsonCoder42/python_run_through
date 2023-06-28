from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, x_axis, y_axis):
        self.snake = []
        self.x_axis = x_axis
        self.y_axis = y_axis

    def snake_add(self, x_axis, y_axis):
        new_section = Turtle(shape="square")
        new_section.penup()
        new_section.color("white")
        new_section.goto(x=x_axis, y=y_axis)
        self.snake.append(new_section)

    def snake_maker(self):
        if len(self.snake) < 3:
            for _ in range(3):
                location = _ * -20
                self.snake_add(location, 0)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)