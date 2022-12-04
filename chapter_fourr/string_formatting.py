s = "hello world"
to_be_found = "e"

for i in range(len(s)):
    if s[i] == to_be_found:
        print(f"{s[i]} was found at index {i}")
        break
else:
    print(-1)

for index, letter in enumerate(s):
    if letter == to_be_found:
        print(f"{letter} was found at {index}")
        break
else:
    print(-1)
