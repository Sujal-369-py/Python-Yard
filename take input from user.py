# in this method we have to seperates elements by  using enter 

n = int(input("Enter number of elements : "))

arr = []

for i in range(n) :
    element = int(input(f"enter element {i + 1} : "))
    arr.append(element)
print(arr)


