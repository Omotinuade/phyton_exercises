number = int(input("Enter a number: "))
i = 1
total = 0
while i < number:
    if number % i == 0:
        total += i
    i += 1

if total == number:
    print("It is a perfect number")

elif total > number:
    print("It is an abundant number")

else:
    print("It is a deficient number")