n = int(input())
count = 0
sum = n

while True:
    if n == 0:
        break

    n = int(input())
    count = count + 1
    sum = sum + n

print(" ")
ave = sum / count


print("The average of these numbers is: {:.2f}".format(ave))
