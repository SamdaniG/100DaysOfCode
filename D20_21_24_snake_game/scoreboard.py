from turtle import Turtle

FONT=("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self,yolo):
        super().__init__()
        self.score=0
        self.highscore=0
        self.highscore=self.read_highscore()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.loc=yolo
        self.goto(0,self.loc-50)
        self.score_update()

    def read_highscore(self):
        with open("highscore.txt","r") as f:
            return int(f.read())

    def write_highscore(self,score):
        #with open("highscore.txt","w") as f:
        with open("../../../../Desktop/highscore.txt","w") as f:    
            f.write(score)

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score}\nHigh Score: {self.highscore}",align="center",font=FONT)


    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
        self.score=0
        self.score_update()
        self.write_highscore(str(self.highscore))
        

    def increment_score(self):
        self.score+=1
        self.score_update()

    def game_over(self):
        self.goto(0,0)
        self.color('white')
        self.write(f"Game Over!",align="center",font=FONT)


