num = int(input("Enter a number : "))
power = 0
decimal = 0

while num > 0:
    digit = num % 10
    if digit == 1:
        decimal += 2 ** power
    power += 1
    num //= 10
print(decimal)
