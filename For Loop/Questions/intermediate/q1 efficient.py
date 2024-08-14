import math

try :
    number = int(input("enter a number : "))

    if number < 0 :
        print("Negative number factorial is not possible")
    else :
        fact = math.factorial(number)
        print("Factorial of number : ",fact)
except ValueError:
    print("error")

