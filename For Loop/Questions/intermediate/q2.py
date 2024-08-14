str = input("Enter here something : ")
# reversed_str = str[::-1]
# print(reversed_str)


reversed_str = ""
for char in str :
   reversed_str = char + reversed_str
print(reversed_str)


