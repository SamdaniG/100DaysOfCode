from turtle import Turtle

from numpy import place

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.penup()

        '''
        self.goto(-300,-250)
        self.pendown()
        self.forward(600)
        self.pu()
        self.goto(-300,250)
        self.pd()
        self.forward(600)
        self.pu()
        '''
        self.goto(0,-280)
        self.pu()
        self.setheading(90)
        #print(self.pos())
        

    def up(self):
        self.fd(10)
        #print(self.pos())

    def starting_pos(self):
        self.goto(0,-280)

    def player_at_end_line(self):
        return self.ycor()>270
            