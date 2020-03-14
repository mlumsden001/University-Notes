import sys

n = int(sys.argv[1])
k = int(sys.argv[2])
i = 2
count = 1
num_list = [i]

while True:
    if k > 0:
        i += 2
        count += 1
    num_list.append(i)
else:
    break
    count = 0
    print(i)
    count += 1
    i += 2
    if count > n:
        break
