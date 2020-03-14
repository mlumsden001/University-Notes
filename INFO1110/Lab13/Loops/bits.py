def most_popular(bin):
    if not isinstance(bin, str):
        return 'TypeError'
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
        return count1
    elif count0 > count1:
        return count0
    else:
        return None

a = most_popular('10110')
b = most_popular('001')
c = most_popular('ABCDEF')
d = most_popular(451)
e = most_popular('101010')

print(a)
print(b)
print(c)
print(d)
print(e)
