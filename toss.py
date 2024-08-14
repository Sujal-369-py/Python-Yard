import random

des = 'Bat', 'Bowl'
toss = 'head', 'tail' 
your_call = input("choice heads or tail : ")
res = random.choice(toss)
if res == your_call :
    print("you won the toss")
    chose = input("choce one Bat or Bawl : ")
    if chose.lower() == "bat" :
        print("you choose to bat")
    else:
        print("you choose to bowl")
else:
    res2 = random.choice(des)
    print("you lose the toss and opponent choice to ",res2)
