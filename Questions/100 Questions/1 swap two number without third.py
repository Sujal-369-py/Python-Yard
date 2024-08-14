def swap(a,b) :
    a = a+b
    b = a-b
    a = a-b
    print("a = ",a, "b = ", b)


a = int(input("Enter a : "))
b = int(input("enter b : "))
print("Before swap ")
print("a = ",a," b = ",b)
print("After swap")
swap(a,b)    