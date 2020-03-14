line = input("Enter colour code here: ")
value = int(line, 16)
red = (value and 0xFF0000)

print(line, "Red: ", value, "Green: ", value, "Blue: ", value)
