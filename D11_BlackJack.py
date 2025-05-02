#This is Day11 of 100DaysOfPython 
import random
import os

quart_card=['A',2,3,4,5,6,7,8,9,10,10,10,10]


def serve_card(a,deck):
    """This serves card from the deck to the list a, from deck"""
    popped_card=deck.pop()
    a.append(popped_card)

def score_check(player,comp):
    if player==comp:
        print("It's a draw!")
    elif player>21:
        print("You lose!")
    elif comp>21:
        print("You win!!")
    elif player>comp:
        print("You win!!")

    else:
        print("You lose!!")

def total_card(incoming):
    deck=incoming.copy()
    
    if 'A' in deck:
        a_count=deck.count('A')
        #print(f"count of A in deck: {deck.count('A')}")
        
        if a_count==2:
            sum_of_aces=[2,12,22]   #[22,12,2]
        elif a_count==1:
            sum_of_aces=[1,11]      #[11,1]
        elif a_count==3:
            sum_of_aces=[3,13,23,33]  #[33,23,13,3]
        elif a_count==4:
            sum_of_aces=[4,14,24,34,44]  #[44,34,24,14,4]
        else:
            sum_of_aces=[0]
        
        for i in range(a_count):
            deck.remove('A')
            #deck.pop('A')
            #print(deck)
        
        new_one=set(deck)-set('A')
        #a_needed=21-sum(new_one)

        a_needed=21-sum(deck)

        init=sum_of_aces[0]
        for i in sum_of_aces:
            if i<=a_needed:
                init=i


        final_sum=sum(new_one)+init

        return final_sum        
    else:
        return sum(deck)

#print(len(complete_deck))
massive_flag=True

decision_to_start=input("Do you want to play a game of Blackjack, y or n?: ").lower()
while massive_flag:
    complete_deck=quart_card*4
    random.shuffle(complete_deck)
#print(complete_deck)

    computer_hand=[]
    player_hand=[]

    #Initial serving of the cards
    serve_card(computer_hand,complete_deck)
    serve_card(player_hand,complete_deck)
    serve_card(computer_hand,complete_deck)
    serve_card(player_hand,complete_deck)

    #player_hand=['A',6]
    os.system('clear')
    #decision_to_start=input("Do you want to play a game of Blackjack, y or n?: ").lower()

    if decision_to_start=='n':
        exit
    else:
        os.system('clear')
        player_hand1=player_hand
        print(f"Your cards: {player_hand1}, current score: {total_card(player_hand1)}")
        
        print(f"Computer's first card: {computer_hand[0]}")
        flag=True
        flag1=True

        if total_card(player_hand)>=21:
            flag=False

        while flag:
            flip_another_card=input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if flip_another_card=='y':
                serve_card(player_hand,complete_deck)
                #print(f"*****")
                os.system('clear')
                print(f"Your cards: {player_hand}, current score: {total_card(player_hand)}")
                print(f"Computer's first card: {computer_hand[0]}")
                if total_card(player_hand)>=21:
                    flag=False
                    flag1=False
            elif flip_another_card=='n':
                flag=False

        
        while flag1:
            if total_card(computer_hand)<17:
                serve_card(computer_hand,complete_deck)
            else:
                flag1=False

        os.system('clear')
        print(f"Your cards: {player_hand}, current score: {total_card(player_hand)}")
        print(f"Computer's cards: {computer_hand}")

        score_check(total_card(player_hand),total_card(computer_hand))

        another_game=input(f"\nDo you want to play another game, y or n? ").lower()
        if another_game=='n':
            massive_flag=False












