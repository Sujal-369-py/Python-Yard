matrix = [
    [1, 2, 3],
    [4, 5, 6,],
    [7, 8, 9]
]
print("Matrix Before ")
for row in matrix :
    print(row)


print("Matrix after ")
new_row = [999,666,333]
matrix.append(new_row)
for row in matrix :
    print(row)


print("Matrix after adding new element")
matrix[3][1] = 36
element = matrix[3][1]
print(element)
