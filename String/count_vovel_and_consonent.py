str = input("Enter a string : ")
vovel = 0
consonent = 0

for char in str :
    if char in 'aeiou':
        vovel+=1
    elif char != " " and char not in '0123456789':
        consonent+=1
print(f"String is : {str}")
print(f"Vovels are : {vovel} \n consonents are : {consonent}")