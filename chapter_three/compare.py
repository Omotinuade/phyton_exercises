largest_number = 0
count = 0
second_largest = 0

while count < 5:
    num = int(input("Enter any number: "))
    if num > largest_number:
        temp = largest_number
        largest_number = num
        second_largest = temp
    count += 1
print("The largest number is ", largest_number, " and the second largest number is ", second_largest)