i = 0

even = i % 2 == 0
in_range = i >= 20 and i <= 200
negative = i < 0
odd = i % 2 == 1

test_pass = (even and in_range) or (odd and negative)
while True:
    i = int(input("Number: "))
    if i == 0:
        break

    if test_pass :
        print("{} passes the test!".format(i))

    elif not test_pass :
            print("{} fails the test!".format(i))

print("Bye!")
