from turtle import Turtle

# keeping values in variables
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    # moving it forward
    def move(self):
        self.forward(MOVE_DISTANCE)

    # goes back to starting position
    def restart(self):
        self.goto(STARTING_POSITION)
