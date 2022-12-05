the_number_of_positives = 0
the_number_of_negatives = 0
sum_of_positives = 0
sum_of_negatives = 0
count = 0

number = int(input("Enter the values , press 0 to end program:"))

while number != 0:
    if number < 0:
        sum_of_negatives = sum_of_negatives + number
        the_number_of_negatives = the_number_of_negatives + 1

    if number > 0:
        sum_of_positives = sum_of_positives + number
        the_number_of_positives = the_number_of_positives + 1

    total = sum_of_negatives + sum_of_positives
    total_number = the_number_of_positives + the_number_of_negatives
    average = total / total_number
    number = int(input("Enter the values , press 0 to end program:"))
    count += 1

else:
    print("No numbers are entered except 0")

print("The number of positives is ", the_number_of_positives)
print("The number of negatives is ", the_number_of_negatives)
print("The total is ", total)
print("The average is ", average)




