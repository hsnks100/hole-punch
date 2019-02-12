import socket

from time import sleep
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = 'abc'
port = 10000;
sock.bind(('', 0))
while True:
    print(data)
    sleep(0.05)
    # 121.159.156.133
    sock.sendto(data.encode(), ('54.180.98.0', port))
    print("send~~~")
    break;

    # data, addr = sock.recvfrom(65535)
    # print(data.decode())


print("step2")
# sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = sock
# sock2.bind((myip, int(pp)))
data, addr = sock2.recvfrom(65535)
dest = (data.decode()).split(',')
dest = (dest[0], int(dest[1]))

while True:
    sleep(0.05)
    # 121.159.156.133
    sock.sendto('home'.encode(), dest)
    data, addr = sock2.recvfrom(65535)
    print(data.decode())
