secreat_num = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit :
    guess = int(input("Make a guess : "))
    guess_count +=1
    if(guess == secreat_num) :
        print("You win !")
        break
else :
        print("you failed !")
    