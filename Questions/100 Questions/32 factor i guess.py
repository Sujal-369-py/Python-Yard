num = 12 
arr = []
k = 3
for i in range(1,num+1): 
    if num%i == 0 : 
        arr.append(i)
for i in range(len(arr)): 
    if k == arr[i]:
        print(i)
print(arr)