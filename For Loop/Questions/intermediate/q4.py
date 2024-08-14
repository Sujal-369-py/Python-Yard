sume = 0
num = int(input("Enter a number : "))
while num>0 :
    r = num%10
    num = num//10
    sume  = (sume * 10) + r
print(sume)
