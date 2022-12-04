x: float = 0
while x < 10:
    print(x, end=" ")
    x += 1

print()
print("The final value is ", x)

count= 0
largest_so_far = 0
while count < 5:
    num = int(input("Give me a number: " ))
    if num > largest_so_far:
        largest_so_far = num

    count += 1

print("The largest number is ", largest_so_far)

count = 0
smallest_num = float("inf")
while count < 5:
    num = int(input("Enter a number"))
    if num < smallest_num:
        smallest_num = num

    count += 1

print("The smallest number is ", smallest_num)