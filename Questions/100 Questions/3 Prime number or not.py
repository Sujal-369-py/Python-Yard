num = int(input('Enter a number : '))
if num ==1 :
    print(num," is not a prime number")
elif num >= 2 :
    for i in range(2,num) :
        if num%i ==0 :
            print(num," is not a prime number")
            break
    else :
        print(num," is a prime number")
 #               This is not effective program


#                        FULLY EFFECTIVE PROGRAM 
def is_prime(num) :
    if num == 1 :
       return False
    elif num == 2 :
       return True
    elif num >2 :
        i = 3
        while  i * i >= num  :
            if i%num ==0 :
               return False
            else :
                return True
        i+=2


n = int(input('Enter a number : '))
if is_prime(n) :
    print(n," is not a prime number ")
else :
    print(n, " is  a prime number ")



