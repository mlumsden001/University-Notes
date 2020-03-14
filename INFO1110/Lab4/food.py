import sys

filename = sys.argv[1]

text_file = open(filename, 'r')

line_text = text_file.readline()

while True:
    print(line_text.split(str(0), end = ""))
    print('\t$', line_text.split(str(1)))
    if line_text == "":
        break
text_file.close()
