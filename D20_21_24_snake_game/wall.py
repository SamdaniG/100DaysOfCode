from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.pensize(3)
        self.color('white')
        
    def create_wall(self,length,width):
        '''Give the length and width of the wall you want to setup.'''
        self.penup()
        self.goto(length,width)
        self.pendown()
        self.setheading(270)
        for a in range(2):
            
            self.forward(width*2)
            self.right(90)
            self.forward(length*2)
            self.right(90)

        self.hideturtle()
