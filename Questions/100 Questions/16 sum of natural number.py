num = int(input("Enter number upto which you want sum : "))
sum =0
for i in range(num+1) :
    sum+=i
    print(i)
print("sum of ",num," natural number is : ",sum)