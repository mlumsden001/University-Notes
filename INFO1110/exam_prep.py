import sys

if len(sys.argv) < 2:
    print('No argument')
    sys.exit()

try:
    sys.argv[1]
except:
    FileNotFoundError('Cannot open file')

f = open(sys.argv[1], 'r')

sum = 0

while True:
    line = f.readline()
    if line[0] == 'e':
        continue
    elif line == '':
        break
    sum += int(line)

print(sum)
