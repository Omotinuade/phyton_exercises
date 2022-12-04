word = "Hello boss baby"


# to_be_found = "b"
for i in range(0, len(word)):
    if word[i] != "b":
        print(word[i], end=" ")

# word = word[0:6] + word[7:11] + word[12] + word[14]
#print("\n")
#print(word.replace("b", " "))
for i in word:
    print(i, end=" ")
for index, letter in enumerate(word):
    print(letter, end=" ")
