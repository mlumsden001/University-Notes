def unt(num):
    if len(num) > 0:
        average = sum(num) / len(num)
        return average
    if len(num) == 0:
        return None

num = []
unt(num)
print(unt(num))
