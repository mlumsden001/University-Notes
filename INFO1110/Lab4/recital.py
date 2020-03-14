import sys

operation = sys.argv[1]

num_list = []
while True:
    n = float(input("Number: "))
    if n == 0:
        break

    num_list.append(n)

print("Your numbers were:")
i = 0
while i < len(num_list):
    print(num_list[i])
    i += 1


avg = sum(num_list) / i
max = num_list[i-1]
min = num_list[0]

while len(sys.argv) < 3:
    if operation == "-sum":
        print("The sum of those numbers is", sum(num_list))
    if operation == "-avg":
        print("The average of those numbers is", avg)
    if operation == "-max":
        print("The largest number is", max)
    if operation == "-min":
        print("The smallest number is", min)
    else:
        sys.exit()
