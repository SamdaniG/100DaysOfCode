#This is Day4 of 100DaysOfCode 
#This is the implementation of Rock, Paper, Scissors Game
from ast import Or
import random

rock='''Rock
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper='''Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor='''Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

choices=[rock,paper,scissor]
computer_choice=random.randint(0,2)
#print(computer_choice)
print("Welcome to the Rock, Paper, Scissors game.")
user_choice=int(input("Press 0 for Rock, 1 for Paper and 2 for Scissors: "))

if user_choice>=0 and user_choice<3:
    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")
    
"""
if user_choice<0 or user_choice>2:
    print("Wrong option chosen!")
elif user_choice>computer_choice:
    print("You win!")
elif user_choice==computer_choice:
    print("It's a draw!")
elif user_choice==0 and computer_choice==2:
    print("You win!")
elif user_choice<computer_choice:
    print("You lose!")

"""
if user_choice<0 or user_choice>2:
    print("Wrong option chosen!")
elif (user_choice==1 and computer_choice==0) or (user_choice==2 and computer_choice==1) or (user_choice==0 and computer_choice==2):
    print("You win!")
elif user_choice==computer_choice:
    print("It's a draw!")
else:
    print("You lose!")
