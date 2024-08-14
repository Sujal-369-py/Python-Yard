num = int(input("Enter up to which you want numbers: "))

for i in range(1, num + 1):
    armstrong = 0
    temp = i
    
    # Calculate the sum of the cubes of the digits
    while temp > 0:
        r = temp % 10
        armstrong += r ** 3
        temp //= 10
    
    # Check if the number is an Armstrong number
    if i == armstrong:
        print(i)