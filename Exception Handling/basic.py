try:
    a = int(input("enter a number : "))
    b = int(input("Enter a number : "))
    result = a/b


except ZeroDivisionError:
    print("Division not possible")


except ValueError:
    print("Invalid values")


else :
    print("Result : ",{result})



finally :  # it will always runs
    print("Division succesfull")