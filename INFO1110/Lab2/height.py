import sys

x = float(sys.argv[1])
x = float(x)

print("The height you have entered is: ", x)

y = x*1.10

print("If you grow by 10% then you'll be {:.3f}".format(y))
