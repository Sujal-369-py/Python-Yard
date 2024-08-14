rows = int(input("Enter number of rows : "))
cols = int(input("Enter number of columns : "))
sym = input("Enter symbol to use : ")
for i in range(rows):
    for j in range(cols):
        print(sym, end="")
    print()