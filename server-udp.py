import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('', 10000))
print("listen: ", 10000)
while True:
    data, addr = sock.recvfrom(65535)
    print("form ip: ", addr[0], "port: ", addr[1])
    # print("echo data: ", data.decode())
    # data = str(addr[1])
    # sock.sendto(data, addr)

# while True:
    # sock.sendto("hello", addr)
    # time.sleep(0.05)
