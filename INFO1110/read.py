def readlines(path):
    lines = []

    f = open(path, 'r')

    next_line = f.readline()
    if next_line == "":
        breaks
    lines.append(next_line.strip())
    f.close()
    return lines

import sys
try:
    path = sys.argv[1]
    lines = readlines(path)
    print("The lines were")
    print(lines)
except IndexError:
    print("Please enter a file path")
