def find_max(numbers):
    max_val = numbers[0]
    for i in numbers:
        if i > max_val:
            max_val = i
    return max_val
