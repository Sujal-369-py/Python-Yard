str = input("Enter a string : ").lower()
count = 0
print("String : ",str)
for char in str:
    if char in 'aeiou':
        count+=1
print(str," contain ",count," vovels")
