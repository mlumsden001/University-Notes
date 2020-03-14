def enqueue(e):
    total = 0
    count = 0
    if size = N:
        return "queue full"
    else:
        last = (first+size) % N
        Q[last] = e
        total += e
        size += 1


def getAverage(total, count):
    if count == 0:
        return "empty queue"
    return total/count

