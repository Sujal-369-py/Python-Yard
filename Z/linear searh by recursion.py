def search(arr,find,i): 
    if arr[i] == find: 
        return 1
    else: 
        return -1 
    search(arr,find,i)
    i+=1

arr = [1,2,3,4,5] 
find = 4 
i = 0 

print(search(arr,find,i))
