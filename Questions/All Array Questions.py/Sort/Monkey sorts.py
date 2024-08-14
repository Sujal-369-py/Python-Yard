import random
import time
arr = [1, 6, 9, 2, 4 ,12]

while arr != sorted(arr):
    
    random.shuffle(arr)
    print(arr)

print("Finally Sorted array : ", arr)
