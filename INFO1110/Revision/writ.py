def writer(filename, lines):
    if not isinstance(filename, str):
        raise TypeError

    if not isinstance(lines, list):
        raise TypeError

    x = open(filename, 'w')
    i = 0
    n = 0

    while n < len(lines):
        if not isinstance(lines[i], str):
            raise TypeError
        n += 1

    while i < len(lines):
        if not isinstance(lines[i], str):
            raise TypeError('List must consist strings')
        x.write(lines[i] + '\n')
        i += 1
    x.close()

lines = ['hi', 'hello', 'hey']

try:
    writer('bean.txt', lines)
    #writer('bean.txt', 1234)
    #writer(1, lines)
except TypeError as e1:
    print(e1)
finally:
    print('ligma')
