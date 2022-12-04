hello = "Hello there!!!"

#print(hello.find("l"))
#print(hello.find("llo"))
# print(hello.index("a"))
# start and stop search of the lowest index of substring
#print(hello.find("e", 3))
#print(hello.find("e", 3, 5))
# when you want to find all the letters in the word
found = 0
while True:
    found = hello.find("e", found)
    if found == -1:
        break
    print(found)
    found += 1
#gets the lowest index from the right
#print(hello.rfind("e"))