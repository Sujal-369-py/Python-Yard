str = input("Enter a string : ")
count = 0

for char in str:
    if char != " ":
        count+=1
print(f"String is : {str} ")
print(f"Total words are : {count}")