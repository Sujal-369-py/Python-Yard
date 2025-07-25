# convert lower case to upper case 
str = input("Enter string in uppercase : ")
new = " "

for char in str : 
    if char == " ": 
        new+=" "
    else: 
        small = ord(char)+32
        new+= chr(small)
print(new)