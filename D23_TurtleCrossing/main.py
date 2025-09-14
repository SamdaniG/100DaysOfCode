from turtle import Turtle,Screen
from player import Player
from car import Car
from scoreboard import Scoreboard

import time




screen=Screen()
screen.setup(600,600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

player=Player()
car=Car()
scoreboard=Scoreboard()

screen.onkeypress(player.up,"Up")



game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    for x in car.all_cars:
        if player.distance(x)<20:
            #screen.update()
            game_is_on=False
            scoreboard.game_over()

    if player.player_at_end_line():
    #if player.ycor()>270:
        player.starting_pos()
        car.increase_speed_car()
        scoreboard.increment_score()


screen.exitonclick()