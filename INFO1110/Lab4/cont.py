xmin = 3
xmax = 7
x = -1

while x < 10:
    x = x+1
    if x < xmin:
        continue
    if x > xmax:
        continue

y = 8 - x
print(x, y)
