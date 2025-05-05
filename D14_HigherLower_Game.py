    #This is Day12 of 100DaysOfPython 
import random

from matplotlib.pylab import rand
from game_data import data
import game_data  
import os

#print(len(data))

random_a=random.randint(0,len(data)-1)  #Better way to tackle this...random.choice(data)
random_b=random.randint(0,len(data)-1)


"""
print(random_a, random_b)   
print(f"{data[random_b]["name"]}, a {data[random_b]["description"]}, from {data[random_b]["country"]}")
print(f"{data[random_a]["name"]}, a {data[random_a]["description"]}, from {data[random_a]["country"]}")

"""
score=0
flag=True
while flag:
    if random_a==random_b:
        random_b=random.randint(0,len(data)-1)

    #print(game_data.higher_lower_art)
    if score>0:
        print(f"That's correct your score is {score}.")
    
    print(f"\nA: {data[random_a]["follower_count"]}")
    print(f"B: {data[random_b]["follower_count"]}\n")
    

    print(f"\033[3mCompare A\033[0m: {data[random_a]["name"]}, a {data[random_a]["description"]}, from {data[random_a]["country"]}")
    #print(game_data.vs_art)
    print(f"\033[3mAgainst B\033[0m: {data[random_b]["name"]}, a {data[random_b]["description"]}, from {data[random_b]["country"]}")
    choice=input("Who has more followers: 'A' or 'B'? ").lower()

    if choice=='a' and data[random_a]["follower_count"]>data[random_b]["follower_count"]:
        score+=1
        #random_a=random_b
        random_b=random.randint(0,len(data))
        os.system('clear')
    elif choice=='b' and data[random_b]["follower_count"]>data[random_a]["follower_count"]:
        score+=1
        random_a=random_b
        random_b=random.randint(0,len(data))
        os.system('clear')
    else:
        flag=False
        os.system('clear')
print(game_data.higher_lower_art)
print(f"Sorry, that's wrong! Final Score: {score}")


    #print("\033[3mThis text is in italics.\033[0m")