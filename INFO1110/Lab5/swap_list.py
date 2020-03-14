def swap_list(a):
    if len(a) < 2:
        pass
    else:
        tmp = a[0]
        a[0] = a[1]
        a[1] = tmp

a = [3, 4]
print("Before swap: a is", a)
swap_list(a)
print("After swap: a is", a)
