# def is_unique(lst):
x = [1, 2, 3, 5, 1]
lst = len(x)
for i in x:
    print(i)
    for ii in range(0, lst, 1):
        print(ii, sep="...")
        if x[i] == x[ii] and x.index(x[i]) != ii:
            outcome = "Not unique"
        #lst.append(i)
print(outcome)

# x = [2, 3, 9, 12, 16, 4, 2, 3]
# is_unique(x)
