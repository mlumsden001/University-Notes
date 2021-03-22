def shortfirst(w):
    schedule = []
    nex = 0
    for j in range(0, len(w) -j -1):
        if w[j][1] > w[j+1][1]:
            temp = w[j]
            w[j] = w[j+1]
            w[j+1] = temp
    for i in range(1, len(w)):
        schedule.append(w[i], nex)
        nex += w[i][1]
    return schedules


w = [(2, 1), (10, 6), (12, 5)]
print(shortfirst(w))