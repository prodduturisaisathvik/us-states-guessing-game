from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 50

    def chances(self):
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(0, 270)
        self.write(f"CHANCES:{self.score}", align="center", font=("arial", 24, "normal"))


    def update_scoreboard(self):
        self.score -= 1
        self.clear()
        self.write(f"CHANCES: {self.score} ", align="center", font=("arial", 24, "normal"))
