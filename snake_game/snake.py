from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.x_axis = 0
        self.y_axis = 0
        self.snake_maker()
        self.head = self.snake[0]
        self.tail = self.snake[-1]

    def snake_add(self, x_spot, y_spot):
        new_section = Turtle(shape="square")
        new_section.penup()
        new_section.color("white")
        new_section.goto(x=x_spot, y=y_spot)
        self.snake.append(new_section)

    def snake_maker(self):
        if len(self.snake) < 3:
            for _ in range(3):
                location = _ * -20
                self.snake_add(location, 0)

    def add_segment(self):
        last_seg = self.snake[-1]
        x = last_seg.xcor()
        y = last_seg.ycor()
        self.snake_add(x, y)

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