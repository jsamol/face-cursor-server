import socket

import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto('l 4'.encode(), (UDP_IP, UDP_PORT))
time.sleep(1)
sock.sendto('r 10'.encode(), (UDP_IP, UDP_PORT))
time.sleep(1)
sock.sendto('u 5'.encode(), (UDP_IP, UDP_PORT))
time.sleep(1)
sock.sendto('d 15'.encode(), (UDP_IP, UDP_PORT))
