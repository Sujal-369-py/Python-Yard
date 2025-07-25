arr = list(map(int,input("Enter array : ").split()))
target = int(input("Enter target : "))
print("Array = ",arr)
print("Target = ",target)

found = False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            print("Target Found at index : ",i," and ",j)
            found = True
            break
    if found:
        break

if not found:
    print("target not found")
    