# numbers = int(input("Enter numbers you want : "))
# for i in range(1,numbers + 1,2) :
#     print(i)



# Now program to print excat how much numbers
numbers = int(input("Enter numbers you want : "))
count = 0
while count !=numbers :
    for i in range(1,numbers+numbers,2) :
        print(i)
        count+=1