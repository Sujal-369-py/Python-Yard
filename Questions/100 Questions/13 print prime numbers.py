num = int(input('Enter a number : '))
for i in range(1,num+1) :
        if num == 2 :
             print(num)
        for i in range(2,num) :
            if num%i !=0 :
                print(num)  
        else :
             break