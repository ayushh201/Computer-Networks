import socket
import time

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.settimeout(5)

server_address = ('127.0.0.1',12345)
pings = 10
rtts, pl = [],0

for i in range(pings):
    start = time.time()
    try:
        message = f"ping {i+1}"
        client_socket.sendto(message.encode(),server_address)
        client_socket.recvfrom(1024)
        rtt = (time.time()-start)*1000
        rtts.append(rtt)
        print(f"ping {i+1} : rtt : {rtt:.2f} ms")
    except socket.timeout:
        print(f"ping {i+1} :packet loss")
        pl += 1



import socket
import random

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('127.0.0.1',12345)
server_socket.bind(server_address)
print("UDP server is running")
while True:
    data,addr = server_socket.recvfrom(1024)
    if(random.random() > 0.7):
        print(f"packet lost from {addr}")
        continue
    print(f"received from {addr} : {data.decode()}")
    server_socket.sendto(data,addr)
