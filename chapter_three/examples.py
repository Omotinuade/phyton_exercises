i = 1
for i in range(1, 101):
    if i % 15 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)

word = "Mississippi is the longest river"
for i, l in enumerate(word):
    print(f"{l}-->{i}")
print(word[27:])
print(word[:-6])
print(word[-5:])
print(word[15:18])
print(word[:8])
print(word[:20:4])
print(word[:-6:-1])
print(word[::-1])
print(word[17:10:-1])
print(word[13:18:-1])
