import socket

from motion import move_left, move_right, move_up, move_down, click

# UDP_IP = "127.0.0.1"
UDP_IP = "0.0.0.0"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(4)  # buffer size is 1024 bytes
    print("received message:", data)

    message = data.decode()
    if message == 'cl':
        click()
    else:
        tab = message.split(' ')
        command, delta = tab[0], int(tab[1])
        if command == 'l':
            move_left(delta)
        elif command == 'r':
            move_right(delta)
        elif command == 'u':
            move_up(delta)
        elif command == 'd':
            move_down(delta)
