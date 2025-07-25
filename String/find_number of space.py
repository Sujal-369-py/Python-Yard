str = input("Enter string : ")
count = 0
for char in str:
    if char == " ":
        count+=1
print(f"string is : {str} and total spaces are : {count}")