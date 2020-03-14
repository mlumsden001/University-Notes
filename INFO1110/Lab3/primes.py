n = int(input("One positive integer please: "))

if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, " is not a prime")
            break
        if not (n % i) == 0:
            print(n, " is a prime")
            break
