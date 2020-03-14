distance = 0.0
walking = True

while walking:
    distance = distance + 10
    if distance > 42.5:
        walking = False

print("Therefore walking is: ", walking)
