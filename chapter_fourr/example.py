count = 0
s = "*"
while count < 2:
    for i in range(1, 21, 2):
        s = "*" * i
        print(s.center(20) * 4)
    count += 1
