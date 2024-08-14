def fab(num):
    a,b=0,1
    if num==0 and num ==1:
        return a
    elif num==2:
        return b
    else :
        return fab(num-1) + fab(num-2)
    

number = int(input("Enter a nmber : "))
fs = fab(number)
print(fs)