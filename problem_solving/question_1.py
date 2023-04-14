def question_1(*args):
    second_largest = 0
    largest = args[0]
    for num in args:
        if num > largest:
            second_largest = largest
            largest = num
        if second_largest < largest:
            largest = second_largest
    return second_largest


print(question_1(5, 3, 2, 1, 4))
