a = 5
b = 3
c = 10
d = 20

tmp = a
a = b
b = tmp

def swap(a, b):
    tmp = a
    a = b
    b = tmp

swap(a, b)
print('a is:', a)
print('b is:', b)

swap(c, d)
print('c is:', c)
print('d is:', d)
