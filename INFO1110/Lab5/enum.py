spam = ['a', 'b', 'c', 'd', 'e']

def my_enum(spam):
    i = 0
    while i < len(spam):
        print("(", i, ",", spam[i], ")", end=" ")
        i += 1
    return

#my_enum(spam)
#e_spam = my_enum(spam)

#print(e_spam)

ham = ['ham', 'spam', 'lamb']
my_enum(ham)
e_ham = my_enum(ham)
print(e_ham)
