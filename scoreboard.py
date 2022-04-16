from turtle import Turtle
from settings import WINDOW_HEIGHT

ALIGNMENT = "center"
FONT = ('Arial',24,'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.hideturtle()
        self.goto(0,(WINDOW_HEIGHT/2)-40)
        self.write(f"{self.score_left}   -   {self.score_right}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self,winner):
        if winner == "left":
            self.score_left += 1
        if winner == "right":
            self.score_right += 1
        game_winner = self.check_game_winner()

        if game_winner:
            self.clear()
            self.goto(0,0)
            self.color("green")
            self.write(f"{game_winner.capitalize()} wins!\n {self.score_left}       -       {self.score_right}", move=False, align=ALIGNMENT, font=FONT)
            return game_winner
        else:
            self.clear()
            self.write(f"{self.score_left}   -   {self.score_right}", move=False, align=ALIGNMENT, font=FONT)
    
    def check_game_winner(self):
        if self.score_left == 4: return "left"
        if self.score_right == 4: return "right"