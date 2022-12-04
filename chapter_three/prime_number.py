i = 1
number = int(input("Enter a number: "))
while i <= number:
    if number % 2 == 1:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
    break


