s = "hello i am sujal" 
res = [word for word in s.split()]
n = len(res)//2
for i in range(n): 
    res[i],res[n-i-1] = res[n-i-1],res[i]
print(res)