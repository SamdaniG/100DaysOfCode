from operator import mod
import random
from turtle import *
from D18_hirst import color_extract

tort=Turtle()
screen=Screen()

#tort.shape('turtle')
tort.speed(10)

def square():
# Creates a square
    for _ in range(4):
        tort.forward(100)
        tort.right(90)

def failed_dashed_line():
    #This is also supposed to create a dashed line
    for a in range(10):
        
        if mod(a,2)==0:
            pendown()
        else:
            penup()
        tort.forward(100)
        
def dashed_line():
    #This creates a dashed line
    for _ in range(10):
        tort.forward(10)
        tort.penup()
        tort.forward(10)
        tort.down()

def polygons():
    for a in range(3,11):

        r=random.random()
        g=random.random()
        b=random.random()
        tort.pencolor(r,g,b)

               
        for side in range(a):
            #print(a)
            angle=360/a
            tort.forward(100)
            tort.right(angle)

def random_walk(num,speed=0):
    tort.pensize(10)
    tort.speed(speed)
    angles=[0,90,180,270]
    #print(random.choice(angles))
    for x in range(num):
        tort.pencolor(rgb_generator())
        tort.forward(30)
        tort.right(random.choice(angles))
    
def rgb_generator():
    r=random.random()
    g=random.random()
    b=random.random()
    return (r,g,b)

def spirograph(num,speed=0):
    for a in range(num):
        tort.speed(speed)
        tort.pencolor(rgb_generator())
        tort.circle(100)
        tort.right(360/num)


hirst_colors=color_extract('image.jpg',20)


colormode(255)
for a in range(-5,5):

    tort.penup()
    tort.home()
    tort.left(90)
    tort.forward(50*a)
    tort.right(90)
    #tort.pos(0,50*a)
    tort.pendown()
    for _ in range(10):
        tort.dot(20,random.choice(hirst_colors))
        tort.penup()
        tort.forward(50)
        tort.pendown()
#tort.home()
#spirograph(60)
#clearscreen()
screen.exitonclick()
