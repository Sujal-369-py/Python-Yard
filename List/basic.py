goal = ["Bramcahrya", "billionaire", "rich", "happy", "peace"]
print("\n",goal)

goal[4] = "inner peace"
print("\n",goal[4])

print("\n",   goal[3:4])   #goal[starting index :  ending index ]

print("\n",   goal[:])   #all list out

for i in range(len(goal)):
    for j in range(len(goal[i])):
        print(goal[i][j],end = "")
    print("    ")