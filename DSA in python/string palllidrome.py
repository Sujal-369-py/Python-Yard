import sys
s = "A man, a plan, a canal: Panama"
l,r = 0,len(s)-1
while l <= r:
    print(s[l]+"  "+s[r])
    if s[l].isalnum() and s[r].isalnum(): 
        low = s[l].lower()
        rig = s[r].lower()

        if low == rig: 
            l+=1
            r-=1
        else:
            print("no")
            sys.exit()
            
    else:
        if not s[l].isalnum():
            l+=1 
        if not s[r].isalnum():
            r-=1
print("yes")
