ran = "aa"
mag = "aab"
ht = {}

for i in range(len(mag)): 
    # if mag[i] in ht:
    #     ht[mag[i]] = ht[mag[i]] + 1
    ht[mag[i]] = ht[mag[i]] + 1

print(ht["a"])
# for i in ht:
#     print(ht[i])
