arr = [1,2,3,0,4,5]
print(arr)
for i in range(len(arr)):
    if arr[i] == 0:
        arr[-1] = arr[i]

print(arr)