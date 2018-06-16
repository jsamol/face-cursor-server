import socket

from motion import click, move

# UDP_IP = "127.0.0.1"
UDP_IP = "0.0.0.0"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, _ = sock.recvfrom(8)
    print("received message:", data)

    message = data.decode()
    if message == 'cl':
        click()
    else:
        tab = message.split(' ')
        # x, y, cl (int, int 0/1)
        x, y, cl = int(tab[0]), int(tab[1]), int(tab[2])
        move(x, y)
        if cl == 1:
            click()
