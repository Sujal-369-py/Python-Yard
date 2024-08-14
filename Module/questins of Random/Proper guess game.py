import random


number = int(input("Enter a number between 0 and 9 : "))
rand = random.randint(0,9)
if rand == number:
    print("you win")
    print("Number was : ",rand)
else :
    print("You lose")
    print("Number was : ",rand)
