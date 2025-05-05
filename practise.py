#PRACTISE 
"""

def total_card(incoming):
    deck=incoming
    
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
        
        #for i in range(a_count):
        new_one=set(deck)-set('A')
            #deck.remove('A')
            #print(deck)
        
        a_needed=21-sum(new_one)

        init=sum_of_aces[0]
        for i in sum_of_aces:
            if i<=a_needed:
                init=i


        final_sum=sum(new_one)+init

        return final_sum        
    else:
        return sum(deck)
"""
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
        
        #new_one=set(deck)-set('A')
        #a_needed=21-sum(new_one)

        a_needed=21-sum(deck)

        init=sum_of_aces[0]
        for i in sum_of_aces:
            if i<=a_needed:
                init=i


        #final_sum=sum(new_one)+init

        final_sum=sum(deck)+init
        return final_sum        
    else:
        return sum(deck)

"""
        for i in sum_of_aces:
            final_sum=sum(deck)+i
            if final_sum>21:
                continue
            else:
                return final_sum

    else:
        return sum(deck)
    """
list=['A',5,5,'A','A','A',10]
list=['A', 6, 7, 7]
sum=total_card(list)
#print(sum)
#print(list)


def is_prime(num):
    #if num ==2:
     #   return True
    
    flag=0
    for i in range(1,num+1):
        if (num%i==0):
            flag+=1
            
    
    if flag==2:
        return True
        
    else:
        return False
        
#print(is_prime(73))

from game_data import data
import random

print(len(data))
print(data[49])

for i in range(0,len(data)):
    print(f"i: {i} random: {random.randint(0,len(data)-1)}")