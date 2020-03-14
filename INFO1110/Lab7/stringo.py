def string(ls):
    if len(ls) == 0:
        return None
    index = 0
    string_list = str()
    while index < len(ls):
        string_list += str(ls[index])
        index += 1
    return string_list

ls = ['a', 'b', 'c']
s = string(ls)
print(s)
