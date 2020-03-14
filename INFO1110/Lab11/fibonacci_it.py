def fib(n):
    l = [0,1]
    i = 2
    while i < n:
        value = l[i-1] + l[i-2]
        l.append(value)
        i += 1

    print(l)
    return l[-1]

#print(fib(8))
