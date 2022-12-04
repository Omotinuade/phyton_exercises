count = 0
largest_number = float("-inf")
smallest_number = float("inf")
number = int(input("enter a number: "))
while number != 0:
    if number > largest_number:
        temp = largest_number
        largest_number = number
    if number < smallest_number:
        smallest_number = number
    number = int(input("enter a number: "))

print("The largest number is", largest_number, "and the smallest number is ", smallest_number)