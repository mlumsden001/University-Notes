n = int(input("Starting number: "))

while n > 1:
    if n % 2 == 0:
        print("{:.0f},".format(n), end = " ")
        n = n / 2

    elif n % 2 == 1:
        print("{:.0f},".format(n), end = " ")
        n = n*3 + 1
print("1")
