dic = {}

arr = [2,7,23,16]
tar = 9

for i in range(len(arr)): 
    com = tar - arr[i] 
    if(dic.get(com)):
       print("Yup we get it")
    else :
        dic[arr[i]] = i 
