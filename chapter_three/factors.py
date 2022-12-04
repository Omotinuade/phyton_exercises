i = 1
total = 0
number = int(input("Enter a number: "))
while i <= number:
    if number % i == 0:
        total += 1
    i += 1

print(number, "has", total, "factors")
