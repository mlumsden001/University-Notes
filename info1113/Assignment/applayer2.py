import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(bytearray(input("Enter a message: ").encode("utf-8")), (sys.argv[1], 10000))
