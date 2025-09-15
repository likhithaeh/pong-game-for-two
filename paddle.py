from turtle import Turtle

class Paddle(Turtle,):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_len=1.5, stretch_wid=8)
        self.color("white")
        self.penup()
        self.goto(pos)

    def up(self):
        self.goto(self.xcor(), y= self.ycor() + 30)

    def down(self):
        self.goto(self.xcor(), y= self.ycor() - 30)