list = [2,3,3,4,4,5,6] 
unique = []
for i in list :
    if i not in unique:
        unique.append(i)
print(unique)