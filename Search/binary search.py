arr = [1, 2, 3, 4, 5]

low = 0
high = len(arr) - 1
mid = (low + high)//2
sech = 4
found = False

while high >= low:
    mid = (low + high) //2
    if arr[mid] == sech:
        found = True
        break
    elif arr[mid] > sech:
        high = mid -1
    elif arr[mid] < sech:
        low = mid + 1
if found:
    print("Item found AT INDEX : ",mid)
else:
    print("Item is not available")