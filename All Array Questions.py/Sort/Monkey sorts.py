import random
import time
arr = [4, 5, 3, 1, 2]
count = 0

while arr != sorted(arr):
    
    random.shuffle(arr)
    print(arr)
    count+=1

print("Finally Sorted array : ", arr)
print("Number of time sorted : ",count)
   