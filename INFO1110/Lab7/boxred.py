def print_box(height):
    if height <= 0:
        return

    width = 2*height
    row = 0
    while row < height:
        column = 0
        while column < width:
            if row == 0 or row == height - 1:
                if column == 0 or column == width - 1:
                    print("+", end='')
                else:
                    print("-", end='')
            else:
                if column == 0 or column == width - 1:
                    print("|", end='')
                else:
                    print(' ', end='')
            column += 1
        row += 1
        print()

import sys

try:
    height = int(sys.argv[1])
    print_box(height)
except ValueError:
    print("must be an int")
except IndexError:
    print("give a height")
