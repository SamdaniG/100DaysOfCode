from mesh import Mesh
from turtle import *
SIDE_LENGTH = 620

import time

screen=Screen()
screen.setup(SIDE_LENGTH+50,SIDE_LENGTH+50)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

mesh=Mesh()

screen.update()

screen.exitonclick()