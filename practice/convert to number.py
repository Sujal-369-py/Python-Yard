phno = (input("Enter your phone number : "))
digit_maping = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : 'five',
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}
output = ""
for i in phno :
    output += digit_maping.get(i,"!") + " "
print(output)