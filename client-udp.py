import socket

from time import sleep
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = 'abc'
port = input('port: ')
sock.bind(('', 0))
while True:
    print(data)
    sleep(0.05)
    # 121.159.156.133
    sock.sendto(data.encode(), ('121.159.156.133', port))
    print("send~~~")

    # data, addr = sock.recvfrom(65535)
    # print(data.decode())
