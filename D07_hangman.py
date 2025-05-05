#This is Day 7 of 100DaysOfCode 
import random

word_list=["aardvark","amoeba","baboon","camel"]
placeholder=""

correct_letters=[]

chosen_word=random.choice(word_list)
for x in chosen_word:
    placeholder+="_"

#print(f"chosen word: {chosen_word}")

#print(f"Placeholder: {placeholder}")
lives=6
game_over=False 
while not game_over:
    print(f"Lives remaining: {lives}")
    display=""
    guess=input("Guess a letter: ").lower()
    #print(f"guess: {guess}")

    for letter in chosen_word:
        if letter==guess:
            display+=guess
            correct_letters.append(guess)
            
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"

    print(f"display :{display}")

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You Lose!")

    if "_" not in display:
        game_over=True
        print("You Win!")