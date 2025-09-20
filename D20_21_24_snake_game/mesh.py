from turtle import Turtle

class Mesh(Turtle):
    def __init__(self,length):
        super().__init__()
        self.color('white')
        self.meshlength=length
        self.shape('classic')
        self.hideturtle()
        
        self.create_mesh(self.meshlength)
        

    def create_mesh(self,yolo):
        a=-int(yolo/2)
        b=-int(yolo/2)

        for x in range(b,-1*b,20):
            #print(f"{a},{x}")
            self.pu()
            self.goto(a,x)
            self.pd()

            #self.goto(a,b)
            self.fd(self.meshlength)

        self.pu()
        self.setheading(270)
        self.goto(-310,310)
        for x in range(a,-1*a,20):
            #print(f"{x},{-1*b}")
            self.pu()
            self.goto(x,-1*b)
            self.pd()

            #self.goto(a,b)
            self.fd(self.meshlength)

        
        
        #self.goto(-300,-300)

        