num_to_divide = int(input("Enter a nummber to divide : "))
divide_with = int(input("Enter a nummber to divide with : "))

short = num_to_divide // divide_with
remainder = num_to_divide - (divide_with * short)

print("Remainder : ",remainder)