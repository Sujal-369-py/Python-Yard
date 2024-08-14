# sum of even and odd numbers sepratly
numbers  = int(input("Enter numbers : "))
sum_of_even = 0
sum_of_odd = 0
while numbers > 0 :
    if numbers %2 == 0 :
        sum_of_even+=numbers
    else :
        sum_of_odd+=numbers
print("Sum of even numbers : ",sum_of_even)
print("Sum of odd numbers : ",sum_of_odd)

    
