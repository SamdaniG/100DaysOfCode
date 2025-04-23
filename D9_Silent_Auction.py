#This is the Day9 of 100DaysOfPython 

import os

escape_bool=True
auctioneers={}
max_val=0
while escape_bool:
    
    name=input("What's your name? ")
    bid_value=int(input("What's your bid? "))
    auctioneers[name]=bid_value
    tbc=input("Are there more persons? yes or no? ").lower()
    os.system('clear')

    if max_val<bid_value:
        max_val=bid_value
        max_person=name

    if tbc=="no":
        escape_bool=False

print(f"The winner is {max_person} with a bid of ${auctioneers[max_person]}.")