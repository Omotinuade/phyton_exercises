list_ = [2, 4, 36, 72, 8, 11]
even = []
odd = []


def arr(lst):
    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(even) == 1:
        return even[0]
    elif len(odd) == 1:
        return odd[0]
    else:
        return None


print(arr(list_))
