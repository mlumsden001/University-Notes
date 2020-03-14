import sys
filename = sys.argv[1]
letter = sys.argv[2]
i = len(sys.argv)

text_file = open(filename, 'r')

while True:
    line_text = text_file.readline()
    if line_text == "":
        break
    elif line_text[0] == letter:
        print(line_text, end = "")
text_file.close()
