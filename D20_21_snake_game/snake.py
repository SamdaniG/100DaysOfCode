from turtle import Turtle, Screen
import time

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
RIGHT=0
LEFT=180
DOWN=270

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    
    def create_snake(self):
        for pos in STARTING_POSITIONS:
            seg=Turtle('square')
            seg.color('white')
            seg.penup()
            seg.goto(pos)
            self.segments.append(seg) 

    def snake_add(self):
        seg1=Turtle('square')
        seg1.color('white')
        seg1.penup()
        new_locx=self.segments[-1].xcor()
        new_locy=self.segments[-1].ycor()
        seg1.goto(new_locx,new_locy)
        self.segments.append(seg1)

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
       

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)