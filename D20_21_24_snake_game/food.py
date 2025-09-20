from turtle import Turtle
import random

from matplotlib.pylab import rand

class Food(Turtle):
    def __init__(self,yolo):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.pu()
        self.yo=yolo
        self.shapesize(stretch_len=0.60,stretch_wid=0.60)
        self.spawn_food(self.yo)

    def spawn_food(self,yolo):
        self.clear()
        yo=yolo
        loc_x=random.randrange(-1*yo,yo,20)
        #loc_x=random.randint(-300,300)
        #loc_y=random.randint(-300,300)
        loc_y=random.randrange(-1*yo,yo,20)
        self.goto(loc_x,loc_y)
        #print(f"{loc_x},{loc_y}")