num = [1, 5, 3, 8, 9 ,12, 420]

def funct(num):
    if len(num) > 0:
        return max(num)
    elif len(num) == 0:
        return None

num = []
funct(num)
print(funct(num))
