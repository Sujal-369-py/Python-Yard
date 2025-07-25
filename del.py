str = "-046" 
new_str = " "
for char in str:
    if char in "123456789":
        new_str+=char
    elif char == "0" or char == '+'or char == '-': 
        pass
    else:
        break 
print(new_str)