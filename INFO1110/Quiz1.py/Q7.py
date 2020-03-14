m = 1
x = int(input("Enter the number of parrots: "))
while m < x:
    if m < x:
        print("Parrot {:.0f} is talking!".format(m))
        m += 1
    if m == x:
        print("Parrot", m, "is talking!")
        print("The parrots have spoken!")
        break
