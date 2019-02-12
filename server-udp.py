import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('', 10000))
print("listen: ", 10000)
addrs = []
while True:
    data, addr = sock.recvfrom(65535)
    addrs.append(addr)
    print("from ip: ", addr[0], "port: ", addr[1])
    sent = False
    for x in addrs:
        for y in addrs:
            if x[0] != y[0]:
                sock.sendto(y[0] + "," + str(y[1]), x)
                sent = True

    if sent == True:
        addrs = []
    # print("echo data: ", data.decode())
    # data = str(addr[1])
    # sock.sendto(data, addr)

# while True:
    # sock.sendto("hello", addr)
    # time.sleep(0.05)
