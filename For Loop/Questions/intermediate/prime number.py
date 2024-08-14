def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

n = int(input("Enter a number: "))  # Convert input to an integer

if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
