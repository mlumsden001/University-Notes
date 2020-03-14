import sys

program = sys.argv[0]
input = str(sys.argv[1])
num = int()
error_message = "Usage: ", program, " (-a | -d)"

if len(sys.argv) == 2:
    if sys.argv[1] == "-a":
        num = 99
        while num < 100 and num > 0 :
            print(num)
            num -= 2
    if sys.argv[1] == "-d":
        num = 1
        while num < 100 and num > 0:
            print(num)
            num += 2

if len(sys.argv) == 1:
    print(error_message)
