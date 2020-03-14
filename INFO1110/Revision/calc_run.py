from calc import Calc

n1 = Calc.add([5, 3, 2, 4, 10])
print(n1)
print('')
print('--')
print('')

n2 = Calc.subtract(10, 8)
print(n2)
print('')
print('--')
print('')

Calc.set_C(3)
n3 = Calc.multiply([6, 'C'])
print(n3)
print('')
print('--')
print('')

Calc.set_B(8)
n4 = Calc.divide(4, 'B')
