counter = 0
largest_number = float("-inf")
smallest_number = float("+inf")
second_maximum = 0

while counter < 5:
    num = int(input('please enter number '))
    if num > largest_number:
        second_maximum = largest_number
        largest_number = num

    if second_maximum < num < largest_number:
        second_maximum = num

    if num < smallest_number:
        smallest_number = num

    counter += 1
print('Largest number is ', largest_number)
print('Smallest number is ', smallest_number)
print('Second largest number is ', second_maximum)
