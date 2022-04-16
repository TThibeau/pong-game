from turtle import Turtle
from settings import WINDOW_HEIGHT,PADDLE_WIDTH,PADDLE_SPEED

class Paddle(Turtle):
    def __init__(self,x_location):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_WIDTH,stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(x_location,0)

    def up(self):
        if self.ycor() <= round(WINDOW_HEIGHT/2) - round(20*PADDLE_WIDTH/2) - 5:
            self.goto(self.xcor(),self.ycor()+PADDLE_SPEED)

    def down(self):
        if self.ycor() >= -round(WINDOW_HEIGHT/2) + round(20*PADDLE_WIDTH/2) + 5:
            self.goto(self.xcor(),self.ycor()-PADDLE_SPEED) 
