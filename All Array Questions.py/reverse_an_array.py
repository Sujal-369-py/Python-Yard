arr = [1, 2, 3, 4, 5]

n = len(arr)

print("Array before swap : ",arr)

for i in range(0,n//2):
   arr[i] , arr[n-i-1] = arr[n-i-1] , arr[i]

print("Array after swap : ",arr)
        
   
