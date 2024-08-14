arr = list(map(int,input("Enter elements : ").split()))

smallest_num = arr[0]
for i in arr :
    if smallest_num > i :
        smallest_num = i

print("smallest number in array : ",smallest_num)