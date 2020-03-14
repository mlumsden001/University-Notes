element = str(input())

def contains(yep):
    if element in yep:
        return True
    else:
        return False

yep = ['nah', 'yeh', 'ah']
contains(yep)
print(contains(yep))
