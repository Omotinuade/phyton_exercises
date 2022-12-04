count = 0
second_largest = float("-inf")
# largest_number = 0
while count < 5:
    num = int(input("Enter any number: "))
    if num > second_largest:
        second_largest = num
    # print("The second largest number is", second_largest)
    if second_largest < largest_number:
        largest_number = second_largest
    count += 1

print("The largest number is ", largest_number, "and the second largest number is", second_largest)
