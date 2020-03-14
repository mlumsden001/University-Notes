def write(function, lines):
    if not isinstance(function, str):
        raise TypeError
    if not isinstance(lines, list, str):
        raise ValueError("Cannot write non-string value to file.")

    f = open(filename, 'w')
    f.write()
