from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 70, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,200)
        self.r_score = 0
        self.l_score = 0
        self.increase_score(0)

    def increase_score(self,player):
        if player == "r":
            self.r_score += 1
        elif player == "l":
            self.l_score += 1
        self.write(f"{self.l_score} | {self.r_score}", align = ALIGNMENT, font = FONT)
