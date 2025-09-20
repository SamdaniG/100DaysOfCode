from turtle import Screen, Turtle
from snake import Snake
from wall import Wall
from food import Food
from mesh import Mesh
from scoreboard import Scoreboard

SIDE_LENGTH = 500

import time

screen=Screen()
screen.setup(SIDE_LENGTH+50,SIDE_LENGTH+50)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

length_param=int(SIDE_LENGTH/2-10)

snake=Snake()
wall=Wall()
food=Food(length_param)
#mesh=Mesh(SIDE_LENGTH)
score=Scoreboard(length_param)

wall.create_wall(SIDE_LENGTH/2,SIDE_LENGTH/2)

screen.listen()
'''
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
'''
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.right,"Right")
screen.onkeypress(snake.left,"Left")

game_is_on=True
#game_is_on=False

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<10:
        #print("Food hit!")
        food.spawn_food(length_param)
        snake.snake_add()
        score.increment_score()
        #game_is_on=False

    if snake.head.xcor()>length_param or snake.head.xcor()<-length_param or \
                snake.head.ycor()>length_param or snake.head.ycor()<-length_param:
        print("wall hit!")
        score.reset()
        snake.reset()
        #game_is_on=False
        #score.game_over()
        #screen.update()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<15:
            print("snake hit!")
            score.reset()
            snake.reset()
            #score.game_over()
            #game_is_on=False


screen.exitonclick()