def question5():
    sum_of_number_divisible_by_3 = 0
    for i in range(1, 30):
        if i % 3 == 0:
            sum_of_number_divisible_by_3 += i
    return sum_of_number_divisible_by_3


print(question5())
