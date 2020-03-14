a = 10
b = 20
c = 6

x = (a < b) and (b > c and (c + 3) < a)
y = ((c < a) or (a > 7)) and ((not (b > 0)) or (b > a))
z = x and y

print(z, x, y)
