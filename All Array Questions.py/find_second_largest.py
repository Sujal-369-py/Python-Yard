arr = [3,2,1]

# Initialize largest and second_largest to negative infinity
largest = float('-inf')
second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest  # The previous largest becomes the second largest
        largest = num  # Update the largest to the current number
    elif num > second_largest and num < largest:
        second_largest = num  # Update the second largest if the current number fits the criteria

print("The second largest element is:", second_largest)
