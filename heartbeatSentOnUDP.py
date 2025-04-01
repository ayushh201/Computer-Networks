import socket
import time

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('127.0.0.1',12345)
server_socket.bind(server_address)
print(f"UDP Heartbeat Server listening on 12345");
last_received = time.time()
while True:
    try:
        server_socket.settimeout(10)
        data,addr = server_socket.recvfrom(1024)
        timestamp = float(data.decode())
        print(f"received heartbeat from {addr} at {timestamp}")
        last_received = time.time()
    except socket.timeout:
        print("client not responding")
        break


import socket
import time

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('127.0.0.1',12345)
while True:
    timestamp = str(time.time())
    client_socket.sendto(timestamp.encode(),server_address)
    print(f"sent heartbeat at {timestamp}")
    time.sleep(5)
