def hail(n):
    sequence = [n]
    if n == 1:
        return sequence
    if n % 2 == 0:
        n = n/2
        sequence.append(n)
    if n % 2 == 1:
        n = 3*n + 1
        sequence.append(n)
    return sequence

print(hail(10))
