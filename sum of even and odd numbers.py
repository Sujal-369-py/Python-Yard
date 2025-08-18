def sum_of_even_odd_numbers(numbers) :
    even_numbers = []
    sum_even = 0
    odd_numbers = []
    sum_odd = 0
    for num in numbers :
        if num%2 == 0 :
            even_numbers.append(num)
            sum_even+=num
        else :
            odd_numbers.append(num)
            sum_odd+=num

    return even_numbers,sum_even,odd_numbers,sum_odd


try :
    numbers = list(map(int,input("Enter numbers : ").split()))
    even_nums,s_even,odd_nums,s_odd = sum_of_even_odd_numbers(numbers)
    print("Even numbers : ",even_nums,"  sum = ",s_even)
    print("Odd numbers : ",odd_nums,"  sum = ",s_odd)
except ValueError:
    print("Wrong input")