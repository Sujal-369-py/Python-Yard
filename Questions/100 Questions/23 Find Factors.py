def find_factors(num):
    for i in range(1,num+1) :
        if num % i == 0 :
            if i==num:
                print(i)
            else:
                    print(i,end=",")
    
