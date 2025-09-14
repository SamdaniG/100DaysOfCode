from turtle import Turtle
import random

from matplotlib.pylab import rand

CAR_MOVING_DISTANCE = 10
MOVE_INCREMENT=5

class Car():
    def __init__(self):
        #super().__init__()
        self.all_cars=[]
        self.car_speed=CAR_MOVING_DISTANCE


    def create_car(self):
        yo=random.randint(1,6)
        if yo == 1:
            new_car=Turtle(shape="square")
            new_car.pu()
            new_car.shapesize(1,2)
            new_car.random_r=random.random()
            new_car.random_g=random.random()
            new_car.random_b=random.random()
            new_car.color(new_car.random_r,new_car.random_g,new_car.random_b)
            new_car.spawn_loc=random.randint(-240,240)
            new_car.goto(320,new_car.spawn_loc)
            new_car.setheading(180)
            #print(f"{new_car.xcor()},{new_car.ycor()}")
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.fd(self.car_speed)

    def increase_speed_car(self):
        self.car_speed += MOVE_INCREMENT

        