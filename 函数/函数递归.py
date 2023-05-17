def sum_numbers(num):
    if num==1:
        return 1
    temp=sum_numbers(num-1)

    return temp    

print(sum_numbers(3))