str = input("Enter a string : ")
old_str = str
reversed_str = ""

for char in str:
    reversed_str = char + reversed_str
if reversed_str == old_str:
    print("Yes, string can be pallidrome ",old_str,"==",reversed_str)
else:
    print("No, string can not  be pallidrome ",old_str,"!=",reversed_str) 