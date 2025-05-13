#This is Day15 of 100DaysOfPython 



import os



NICKEL_VALUE=0.05
QUARTER_VALUE=0.25
DIME_VALUE=0.10
PENNY_VALUE=0.01

def money_calc(quarters,dime,nickel,penny):
    value=QUARTER_VALUE*quarters+DIME_VALUE*dime+NICKEL_VALUE*nickel+penny*PENNY_VALUE
    return value
          

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources_filled={
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}


drinks=["espresso","latte","cappuccino"]

flag=True
#flag=False

tolerance=3
insufficient_resources=set()

print("Here's the menu:")
for a in MENU:
    print(f"{a}= ${MENU[a]["cost"]}")
print("\n")

while True:
    drink_choice=input("What would you like? (espresso, latte, cappuccino): ").lower()


    if drink_choice=="report":
        for a in resources:
            print(f"{a} = {resources[a]}")
        print(f"money= ${money["value"]:0.2f}\n")
        continue

    if drink_choice=="refill":
        print("Resources refilled!!\n")
        resources=resources_filled
        insufficient_resources=set()
        continue

    if drink_choice=="off":
        exit()


    if drink_choice not in drinks:
        print("That was an incorrect input. Try again\n")
        #os.system('clear')
        tolerance-=1
        continue
        
    flag_num=0
    ingredients_individual=MENU[drink_choice]["ingredients"]

    for a in ingredients_individual:
        if ingredients_individual[a]<resources[a]:
            flag_num+=1
        else:
            insufficient_resources.add(a)


    if flag_num<len(ingredients_individual):
        print(f"Insufficient resources!")
        print(f"You are missing the following: ")
        for a in insufficient_resources:
            print(f"{a}")
        print("\n")
        continue
    


    if tolerance==0:
        print("You are an imbecile!!")
        exit()





    print("\nInsert the change.")
    quarters=int(input(f"Quarters: "))
    dime=int(input("Dimes: "))
    nickel=int(input("Nickels: "))
    penny=int(input("Penny: "))
    print("\n")
    money_paid=money_calc(quarters,dime,nickel,penny)



    if money_paid>MENU[drink_choice]["cost"]:
        change=money_paid-MENU[drink_choice]["cost"]
        print(f"The cost of the {drink_choice} is ${MENU[drink_choice]["cost"]}, here's your money ${change :0.2f}.")
        money["value"]+=money_paid
    else:
        print(f"The money slotted is {money_paid:02}, and that is less than {MENU[drink_choice]["cost"]}. Amount refunded.\n")
        continue
    
    if flag_num==len(ingredients_individual):
        print(f"Here's your {drink_choice}. Enjoy!!\n")
        for a in ingredients_individual:
            resources[a]-=MENU[drink_choice]["ingredients"][a]

