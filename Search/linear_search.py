array = [1,2,5,4,7,8,9]
sec = 2
found = False
for i in range(len(array)):
    if array[i] == sec:
        found = True
        break
if found:
    print("Item founded at index ",i)
else:
    print("Item not founded")