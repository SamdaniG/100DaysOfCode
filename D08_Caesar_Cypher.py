#This is Day7 of 100DayOfPython 
import os

def caesar(direction,text,shift):
    if direction=="decrypt":
        shift*=-1
    cypher_text="" #samdani
    for x in text:
        if x not in alphabets:
            cypher_text+=x
        else:
            loc=alphabets.index(x)
            final_shift=(loc+shift)%len(alphabets)
            cypher_text+=alphabets[final_shift]
            #print(x,loc,cypher_text)
    print(f"Here's the {direction}ed result: {cypher_text}")


"""
def encrypt(text,shift): 
    cypher_text="" #samdani
    for x in text:
        loc=alphabets.index(x)
        final_shift=(loc+shift)%25
        cypher_text+=alphabets[final_shift]
        #print(x,loc,cypher_text)
    print(f"Here's the encoded result: {cypher_text}")
    #return cypher_text


def decrypt(text,shift):
    cypher_text="" #samdani
    for x in text:
        loc=alphabets.index(x)
        final_shift=(loc-shift)%25
        cypher_text+=alphabets[final_shift]
        #print(x,loc,cypher_text)
    print(f"Here's the encoded result: {cypher_text}")
    #return cypher_text
"""
to_be_continued=True
while to_be_continued:

    alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    direction=input("What do you wanna do, encrypt or decrypt? ").lower()
    text=input("Enter the text:- ").lower()
    shift=int(input("Type the shift number: "))

    caesar(direction,text,shift)
    restart=input("Do you wanna run the program again, yes or no? ").lower()
    os.system('clear')

    if restart=="no":
        to_be_continued=False