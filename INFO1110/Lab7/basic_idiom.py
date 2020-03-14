words = ['Collie', 'Retriever', 'Corgi', 'Labrador', 'Husky', 'Malamute']

def longest(words):
    if len(words) == 0:
        return None

    longest_len = -1
    longest_index = -1

    index = 0
    while index < len(words):
        next_word = words[index]
        if len(next_word) >= longest_len:
            longest_len = len(next_word)
            longest_index = index

        index += 1

    return words[longest_index]

def shortest(words):
    if len(words) == 0:
        return None

    shortest_len = len(words[0])
    shortest_index = 0

    index = 0
    while index < len(words):
        next_word = words[index]
        if len(next_word) <= shortest_len:
            shortest_len = len(next_word)
            shortest_index = index

        index += 1
    return words[shortest_index]

def av_len(words):
    if len(words) == 0:
        return None
    tot_len = 0
    index = 0
    while index < len(words):
        next_word = words[index]
        tot_len += float(len(next_word))
        index += 1
    ave = tot_len / index
    return ave

def start_count(words, ch):
    if len(words) == 0:
        return None
    index = 0
    next_word = words[index]
    count = 0
    while index < len(words):
        next_word = words[index]
        if next_word[0] == ch:
            count += 1
        index += 1
    return count

words = ['Collie', 'Retriever', 'Corgi', 'Labrador', 'Husky', 'Malamute']
l = longest(words)
s = shortest(words)
a = av_len(words)
c = start_count(words, 'C')
d = start_count(words, 'D')
h = start_count(words, 'H')

print(l)
print(s)
print(a)
print(c)
print(d)
print(h)
