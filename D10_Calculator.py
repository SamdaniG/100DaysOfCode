#This is Day10 of 100DaysOfPython 
import os

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b


calculator_dict={}

calculator_dict["+"]=add
calculator_dict["-"]=subtract
calculator_dict["*"]=multiply
calculator_dict["/"]=divide

#print(calculator_dict["*"](4,5))
tbc=True
tbc_master=True
while tbc_master:
    n1=float(input("Enter the first number: "))
    tbc=True
    while tbc:
        #n1=input("Enter the first number: ")
        sign=input("Enter the operation you want to do, + - * / : ")
        n2=float(input("Enter the second number: "))
        ans=calculator_dict[sign](n1,n2)
        print(f"{n1} {sign} {n2} = {ans}\n")
        decision=input(f"Type 'y' to continue calculating from {ans}, or type 'n' to start a new calculation, or 'q' to quit: ")
        if decision=='y':
            n1=ans
            os.system('clear')
        elif decision=='n':
            tbc=False
            os.system('clear')
        else:
            tbc=False
            tbc_master=False