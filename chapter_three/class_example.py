number = int(input("Enter a number: "))
largest_number = number
smallest_number = number
while number != 0:
    number = int(input("Enter another number or enter 0 to quit: "))
    if number > largest_number:
        largest_number = number
    if number < smallest_number:
        smallest_number = number
print("The smallest number is ", smallest_number, "The largest number is ", largest_number)