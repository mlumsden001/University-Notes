import sys

x = sys.argv[1] #x is the first number
y = sys.argv[2] #y is the second number

x = int(x)
y = int(y)

print(" ")
print("Your argument list is: ", len(sys.argv), "numbers.")
print("Argument: ", str(sys.argv))
print(" ")
print("Add +: ", x+y)
print("Sub -: ", x-y)
print("Mult *: ", x*y)
print("Div /: ", x/y)
