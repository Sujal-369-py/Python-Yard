arr = list(map(int,input("Enter array : ").split()))
target = int(input("Enter target : "))

print("array = ",arr)
print("Target = ",target)

found = False
for i in range(len(arr)):
    if arr[i]==target or arr[i]+arr[i]==target:
        print("targer found at index ",i)
        found = True
        break
    for j in range(i+1,len(arr)):
        if  arr[i]+arr[j]==target:
            print("target found in index ",i,"and",j)
            found = True
            break
    if found:
        break

if not found:
    print("Target not found")
