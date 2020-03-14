import sys

def consonant(ch):
    if len(ch) != 1:
        return False
    c = ch[0]
    if c == 'a' or c =='e' or c == 'i' or c == 'o' or c == 'u':
        return False
    else:
        return True

if len(sys.argv) < 2:
    print("Please give a character")
    sys.exit(1)
else:
    ch = sys.argv[1]
    is_consonant = consonant(ch)
    if is_consonant:
        print(ch, "is a consonant")
    else:
        print(ch, "is not a consonant")
