arr = [0] * 26
s = "ab"
words = ["ad","bd","aaab","baa","badab"]
for i in s: 
    arr[ord(i)-97] = 1
m = 0
c = 0
for i in range(len(words)):
    for j in range(len(words[i])):
        index = ord(words[i][j])
        if arr[index] == 1:
            m+=1
            continue
    if m == len(words[i-1])-1:
        c+=1
return c