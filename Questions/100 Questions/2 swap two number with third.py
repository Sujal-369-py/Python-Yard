def swap(a,b) :
   c = a
   a = b
   b = c
   return a,b


a,b = int(input("Enter a and b : "))
print("Before swap ")
print("a = ",a," b = ",b)
print("After swap ")
swap(a,b)
print("a = ",a," b = ",b)