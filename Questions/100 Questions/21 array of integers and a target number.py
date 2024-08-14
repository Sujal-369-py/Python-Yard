arr = [2,7,11,18]
target = 90
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]  + arr[j] == target:
            print(i,j)
            break
else:
    print("cant find match")