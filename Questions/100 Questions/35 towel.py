str = input("Enter a string : ")
new = " "
for char in str :
    loop = ord(char)
    if char == " ": 
        new+=" "
    elif loop in range(ord('a'),ord('z')):
        big = ord(char)-32
        new+= chr(big)
    elif loop in range(ord('A'),ord('Z')): 
        small = ord(char)+32
        new+= chr(small)
print(new)