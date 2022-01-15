import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# setting up tne screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
# turned off the tracer
screen.tracer(0)

# creating player object and controlling it
player = Player()
screen.listen()
screen.onkey(player.move, "Up")

car = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    # getting the screen to update every 0.1 second
    time.sleep(0.1)
    screen.update()
    # creating the car object
    car.create_car()
    # moving the car
    car.move_car()

    # detect if turtle reaching the final line
    if player.ycor() > 280:
        # player going back to original position
        player.restart()
        # update the score every time it finishes
        score.update()
        # increment the speed of the car
        car.increment()

    # detect collision with car and stops the game
    for i in car.car_list:
        if i.distance(player) < 20:
            game_is_on = False
            # show game over in screen
            score.game_over()

screen.exitonclick()
