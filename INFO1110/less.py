import sys

line = less.readline()

def read(file):
    with open(sys.argv[2], r) as less:
        while True:
            n = input()
            if n == "":
                print(line)
            if n == "q":
                break
    return ""

print(line)
n = input()
read(n)
