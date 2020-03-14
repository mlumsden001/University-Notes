import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 10000))
while True:
    data, address = s.recvfrom(256)
    print("Message from %s: %s" % (str(address), data))
