i = 1
while i <= 100:
    if i % 5 == 0 and i % 3 == 0:
        print("fizz buzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
       print(i)
    i += 1

word = "Hello world"
for letter in word:
    print(letter, end=" ")
