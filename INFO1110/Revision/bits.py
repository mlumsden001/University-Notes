def most_popular(bin):
    if not isinstance(bin, str):
        raise TypeError
    i = 0
    count1 = 0
    count0 = 0
    while i < len(bin):
        if bin[i] == '1':
            count1 += 1
        elif bin[i] == '0':
            count0 += 1
        else:
            return 'ValueError'
        i += 1

    if count1 > count0:
        return 1
    elif count1 < count0:
        return 0
    elif count1 == count0:
        return None

bin = '1011'
x = most_popular(bin)
print(x)
