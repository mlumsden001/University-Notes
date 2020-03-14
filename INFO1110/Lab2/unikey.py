#w1 = "Mitchel"
#w2 = "Lumsden"

#print("Your name is: ", w1, w2)

#message = 'Mitchel'.split('itchel', sep=0) + 'Lumsden'.split('sden', sep=0)


#rint("Your unikey is: ", message)

#print("Your unikey is: ", w1[0] + w2[0] + w2[1] + w2[2] + "7853")


name = input()
name_given = name.split()
first_name = name_given[0]
second_name = name_given[1]


print("Your name: " + name)

import random

number = random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9)
number = str(number)
last_name = second_name[0] + second_name[1] + second_name[2]
first_initial = first_name[0]
final = first_initial + last_name + number
print("Your Unikey is: {}".format(final))
