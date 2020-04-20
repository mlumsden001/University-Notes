def mode(A):
    values = {}
    for i in A:
        if i in values.keys():
            values.update({i: values.get(i) + 1})
        else:
            values[i] = 1
    mode_key = values[A[0]]
    # return values
    for j in values:
        if values.get(j) > values.get(mode_key):
            mode_key = values[j]
    print(values)
    return mode_key

A = [1, 2, 4, 5, 6, 3, 4, 4, 2, 12, 4, 5, 23]
print(mode(A))

    

