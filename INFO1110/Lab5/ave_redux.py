ls = [5, 3, 2, 4, 10]

def average(ls):
    mean = ls[0-4] / 5
    if len(ls) == 0:
        print("There is no average!")
        return None
    if len(ls) > 0:
        print("The mean of the numbers is:", mean)
        return yy = list(enumerate(ls))

yy = average(ls)
print(yy[0], yy[1])
