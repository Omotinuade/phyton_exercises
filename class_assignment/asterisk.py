def star(x):
    count = 1
    for i in range(0, x,  1):
        for j in range(0, i+1):
            print("*", end=" ")
        print()






star(7)
