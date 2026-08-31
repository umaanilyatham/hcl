def second_max(list):
    first_max = second_max = float('-inf')
    for num in list:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif first_max > num > second_max:
            second_max = num
    return second_max

print(second_max([1, 2, 3, 4, 5,20]))


