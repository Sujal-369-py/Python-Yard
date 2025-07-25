arr = [3,6,9]
print(arr)

# append put element to last position
arr.append(10)
print(arr)

#extent extent list 
arr.extend([11,12,13])
print(arr)

#insert inserts elemnt to desired position
arr.insert(0,1)
print(arr)

#remove removes particular element from list by name of element
arr.remove(9)
print(arr)

#pop remove last element from list if empthy or it remove particular element by index
arr.pop()
print(arr)


# It clears the whole array
# arr.clear()
# print(arr)

# index it retturn the index value
#index(element, start, end)
print(arr.index(3,0,4))

#count return the number of element is present
print(arr.count(12))



#it basically sort the array
# sort(reverse =  it reverses the array (if True), abs = it sort arrau=y in abosute form)
# arr = [5, 2, 9, 1, 7]

# # Sort in ascending order
# arr.sort()
# print(arr)  # Output: [1, 2, 5, 7, 9]

# # Sort in descending order
# arr.sort(reverse=True)
# print(arr)  # Output: [9, 7, 5, 2, 1]

# # Sort with a custom key (e.g., by absolute value)
# arr = [-3, -1, -4, 2, 0]
# arr.sort(key=abs)
# print(arr)  # Output: [0, -1, 2, -3, -4]

arr.sort(reverse=True)
print(arr)

# basically it copy one array from other
arr2 = arr.copy()
print(arr2)


#                                                               -----More functions--------

print(" maximun in array : ",max(arr))
print(" minimum in array : ",min(arr))
print(" length of  array : ",len(arr))
print(" sum of array : ",sum(arr))

ls = "rich"
n = list(ls)
print(n)