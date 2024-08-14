# num = int(input("Enter a number : "))

# final = ""

# print("decimal form : ",num)

# if num ==0:
#     final = "0"

# while num > 0:
#     digit = num%2
#     final = str(digit) + final  #coverting decimal to binary
#     num//=2
# print("binary Form : ",final)





# without coverting decimal to binary
n = int(input("Enter anumber : "))

binary = 0
place = 1

print("decimal form : ",n)

while n > 0:
    digit = n%2
    binary+=digit * place
    n//=2
    place*=10
print("binary form : ",binary)

