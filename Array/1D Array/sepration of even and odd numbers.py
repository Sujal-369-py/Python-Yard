def even_odd_numbers(numbers) :
    even_num = []
    odd_num = []
    for nums in numbers:
        if nums%2 ==0 :
            even_num.append(nums)
        else :
            odd_num.append(nums)

    return even_num,odd_num

try :
    numbers = list(map(int,input("Enter integer seprated by space :  ").split()))
    even_number , odd_number = even_odd_numbers(numbers)
    print("Even numbers : ",even_number)
    print("odd numbers : ",odd_number)
except ValueError:
    print("You had given wrong input")