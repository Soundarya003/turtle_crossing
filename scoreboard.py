from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "LEFT"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.score_card()

    def score_card(self):
        self.write(arg=f"Level: {self.count}", font=FONT, align=ALIGN)

    def update(self):
        self.count += 1
        # important
        # it clears the previous score and updates the score
        self.clear()
        self.score_card()

    def game_over(self):
        self.goto(x=-40, y=0)
        self.write(arg=f"GAME OVER!!", move=False, align=ALIGN, font=FONT)
