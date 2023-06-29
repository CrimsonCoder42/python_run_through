from turtle import Turtle

class SnakeScoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.reset()

    def reset(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.r_score, align='center', font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.l_score, align='center', font=("Courier", 80, "normal"))

    def point(self, player):
        if player == "left":
            self.l_score += 1
            self.reset()
            print(self.r_score)
        if player == "right":
            self.r_score += 1
            self.reset()
            print(self.r_score)