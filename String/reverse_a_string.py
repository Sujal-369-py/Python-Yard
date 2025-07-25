str = input("Enter a string : ")
actual_str = str
reversed_str = ""

for char in str:
    reversed_str = char + reversed_str
print(f"Actual string : {actual_str} and Reversed string : {reversed_str}")