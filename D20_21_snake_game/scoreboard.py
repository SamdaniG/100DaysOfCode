from turtle import Turtle

FONT=("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self,yolo):
        super().__init__()
        self.level=0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.loc=yolo
        self.goto(0,self.loc-50)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.level}",align="center",font=FONT)

    def increment_score(self):
        self.level+=1
        self.score_update()

    def game_over(self):
        self.goto(0,0)
        self.color('white')
        self.write(f"Game Over!",align="center",font=FONT)


