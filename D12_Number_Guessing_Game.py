#This is Day12 of 100DaysOfPython 
import random
import os

HARD_LEVEL=5
EASY_LEVEL=5+5

def check_guess(guess):
    global the_number,difficulty_level,flag

    if the_number==guess:
        print(f"You got it!. The number was indeed {guess}.")
        flag=False
    elif the_number>guess:
        difficulty_level-=1
        print("Too low.")
    else:
        difficulty_level-=1
        print("Too high.")       
    
    if difficulty_level!=0:
        print("Guess again!")

    if difficulty_level==0:
        print(f"You have run out of guesses. Boo! The number I was thinking is {the_number}")
        flag=False 




art=r'''

  ________                                __  .__                                 ___.                ._.
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   ___________| |
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \ |
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/\|
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   __
        \/            \/     \/     \/             \/     \/       \/            \/    \/     \/       \/


'''
massive_flag=True
while massive_flag:
    print(art)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100!")
    flag= True
    tries_to_get_it_right=3
    while flag:
        diff_level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if diff_level=='easy':
            difficulty_level=EASY_LEVEL
            flag=False
        elif diff_level=='hard':
            difficulty_level=HARD_LEVEL
            flag=False
        else:
            if tries_to_get_it_right==0:
                print("\nYou are an imbecile! Exiting the program!")
                exit()        
            tries_to_get_it_right-=1
            print("Wrong input! Try again.")




    the_number=random.randint(1,100)
    #print(the_number)

    flag=True
    while flag:
        print(f"You have {difficulty_level} attempts to guess the number.")
        guess=int(input("Make a guess: "))
        check_guess(guess)

    #    print("Guess again.")
    massive_flag_check=input("\n\nDo you want to play the game again?: y or n: ")
    if massive_flag_check=='n':
        massive_flag=False
    else:
        os.system('clear')




