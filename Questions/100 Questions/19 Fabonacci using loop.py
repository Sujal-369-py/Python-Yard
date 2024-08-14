# def fabo(num):
#     a,b=0,1
#     if num ==0 and num==1:
#         print(a)
#     elif num==2:
#         print(b)
#     else :
#         for i in range(3,num,1) :  #upto num for eg if num is 30 then it will print 30 fabonacci numbers
#             c = a+b
#             print(c)
#             a=b
#             b=c


# n = int(input("Enter a number : "))
# fabo(n)



# n = int(input("Enter a number : "))
# a,b=0,1
# print(a)
# print(b)
# for i in range(3,n,1):
#     c=a+b
#     print(c)
#     a=b
#     b=c
    

# Upt n numbers 
n = int(input("Enter a number : "))
a,b=0,1
print(a)
print(b)
for i in range(3,n,1) :
    while i>=n:
    
        c=a+b
        print(c)
        a=b
        b=c