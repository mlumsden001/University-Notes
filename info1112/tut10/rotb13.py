import string

line = input()

alpha = string.ascii_lowercase

i = 0

newLine = ""

while i < len(line):

    if line[i].isalpha():
        index = line.index(line[i])
        newLine += alpha[(index+13)%26]
    else:
        newLine += line[i]
    i += 1

print(newLine)
