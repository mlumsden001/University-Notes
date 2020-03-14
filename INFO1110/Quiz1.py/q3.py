a = 1
m = 2
y = 5
if a > y:
    y = -y
    m = 1 + m
if y <= 5:
    a = 2*(a+y)
else:
    pass
if m < 2*y:
    m = m - 1
else:
    pass

if y < a:
    y = 1
else:
    pass

y = 3*y + m

print(a, m, y)
