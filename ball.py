from turtle import Turtle
from settings import BALL_SIZE,BALL_SPEED,WINDOW_HEIGHT,x_location_left,x_location_right,PADDLE_WIDTH
from random import randint,choice
direction = [-BALL_SPEED,BALL_SPEED]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=BALL_SIZE,stretch_wid=BALL_SIZE) 
        self.speed("fastest")
        self.goto(0,0)
        self.y_velocity = randint(-BALL_SPEED,BALL_SPEED)  # pixels/(time of iteration)
        self.x_velocity = choice(direction)  # pixels/(time of iteration)

    def move(self,left_paddle_ycor,right_paddle_ycor):
        self.sety(self.ycor() + self.y_velocity)
        self.setx(self.xcor() + self.x_velocity)
        self.check_bounce(left_paddle_ycor,right_paddle_ycor)
        winner = self.check_game_over()
        return winner

    def check_bounce(self,left_paddle_ycor,right_paddle_ycor):                  # Checks for bounce against upper/lower wall, paddle and bounces the ball
        if self.ycor() >= round(WINDOW_HEIGHT/2) - round(20*BALL_SIZE/2) - 5:   # Upper bound
            self.y_velocity = -self.y_velocity

        if self.ycor() <= -round(WINDOW_HEIGHT/2) + round(20*BALL_SIZE/2) + 5:  # Lower bound
            self.y_velocity = -self.y_velocity

        if self.distance((x_location_left,left_paddle_ycor))< PADDLE_WIDTH*11 and self.xcor() == x_location_left+BALL_SIZE*10: 
            self.x_velocity = -self.x_velocity

        if self.distance((x_location_right,right_paddle_ycor))< PADDLE_WIDTH*11 and self.xcor() == x_location_right-BALL_SIZE*10:   
            self.x_velocity = -self.x_velocity

    def check_game_over(self):
        if self.xcor() < x_location_left:
            self.color("red")
            return "right"

        if self.xcor() > x_location_right:
            self.color("red")
            return "left"
        
    def reset(self):
        self.color("blue")
        self.goto(0,0)
        