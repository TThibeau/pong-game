from time import sleep
import tkinter
import os
from paddle import Paddle 
from ball import Ball
import game_screen
from scoreboard import Scoreboard
from settings import x_location_left,x_location_right,WINDOW_HEIGHT,WINDOW_WIDTH,SLEEP_TIME

os.system('cls || clear')

# Make the paddles
paddle_left = Paddle(x_location_left)
paddle_right = Paddle(x_location_right)

# Make the screen
game_screen.draw_broken_line(WINDOW_HEIGHT)
screen = game_screen.draw_background(WINDOW_WIDTH,WINDOW_HEIGHT)

# Make the ball
ball = Ball()

# Make the scoreboard
scoreboard = Scoreboard()

# Listen for the keypresses
screen.listen()
screen.onkeypress(paddle_right.up,"Up")
screen.onkeypress(paddle_right.down,"Down")
screen.onkeypress(paddle_left.up,"w")
screen.onkeypress(paddle_left.down,"s")

game_is_on = True
while game_is_on:
    round_winner = ball.move(paddle_left.ycor(),paddle_right.ycor())
    screen.update()

    if round_winner:
        game_winner = scoreboard.update_score(round_winner)
        if game_winner:
            game_is_on = False
        else:
            sleep(2)
            ball.reset()
    sleep(SLEEP_TIME)

tkinter.mainloop()