# convert lower case to upper case 
str = input("Enter string in lowercase : ")
new = " "

for char in str : 
    if char == " ": 
        new+=" "
    else: 
        big = ord(char)-32
        new+= chr(big)
print(new)