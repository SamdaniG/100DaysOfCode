#This is Day2 of 100DaysOfCode Challenge 
print("Welcome to the tip calculator!")
"""
bill=input("What was the total bil? $")
tip=input("How much tip would you like to give?10, 12 or 15 ")
split=input("How many people are splitting the bill? ")
print(f"Each person should pay: ${int(bill)*(1+int(tip)/100)/int(split)}" )

"""
bill=float(input("What was the total bil? $"))
tip=int(input("How much tip would you like to give?10, 12 or 15 "))
split=int(input("How many people are splitting the bill? "))
final_amount=round(bill*(1+tip/100)/split,2)

#print(final_amount)
print(f"Each person should pay: ${final_amount}")
