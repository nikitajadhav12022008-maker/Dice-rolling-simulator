import random as rd

while True:
    print("dice:", rd.randint(1,6))
    if(input("roll again? (y/n):") != 'y'):
        break


