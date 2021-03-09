from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-200, 250)
        self.level = 1
        self.score()

    def score(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.score()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
