arr = [1, 3, 2, 9 ,5, 8]
arr2 = []
check = arr[0]
for i in range(len(arr)):
        if arr[i] < check :
            check = arr[i]
            arr2.append(arr[i])
print(arr2)
