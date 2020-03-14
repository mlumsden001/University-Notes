def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero') #raise exits the function if True
    return a / b

a = input('Numerator: ')
b = input('Denominator: ')

try:
    x = int(a)
    y = int(b)
    n = divide(x, y)
    print('Result {}'.format(n))
except ZeroDivisionError as e: #as establishes e as the variable for ZeroDivisionError
    print(e)
except ValueError:
    print('What happened?')
except Exception:
    print('Will I ever trigger?')
finally:
    print('I always have the last laugh :D')
