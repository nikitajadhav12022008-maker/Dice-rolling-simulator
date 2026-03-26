#python based dice rolling simulator:
#importing random module
import random as rd
#while loop running
while True:
    print("dice:", rd.randint(1,6))
    #conditional statements
    if(input("roll again? (y/n):") != 'y'):
        break




