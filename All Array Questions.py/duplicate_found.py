arr = list(map(int,input("Enter array : ").split()))

Duplicate_fd = 0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            value = arr[i]
            Duplicate_fd+=1
print("duplicates found of",value, "and they are : ",Duplicate_fd)