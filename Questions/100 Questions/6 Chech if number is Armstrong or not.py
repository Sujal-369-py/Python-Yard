num = int(input("Enter a number : "))
armstrong = 0
cross = num  # directly we cant do that because the value of num == 0 at the end of loop
while num > 0 :
    r = num%10
    num//=10
    armstrong += r*r*r

if cross == armstrong :  # so due to this we have to put the initial value of num to another variable
    print(cross," is a Armstrong number")
else :
    print(cross," is not a Armstrong number")