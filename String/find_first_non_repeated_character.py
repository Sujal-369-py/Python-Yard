str = "swiss"

for char1 in str:
    for char2 in char1+1:
        if char1 != char2:
             print(char1," is first non repeating character ")