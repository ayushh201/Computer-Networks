import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('127.0.0.1',12345)
server_socket.bind(server_address)
print("udp is listening on port 12345")
while True:
    data,client_address = server_socket.recvfrom(1024)
    print(f"Received msg from {client_address} : {data.decode()}")
    response = "msg received"
    server_socket.sendto(response.encode(),client_address)



import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('127.0.0.1',12345)
message = "hello udp"
client_socket.sendto(message.encode(),server_address)
data,_ = client_socket.recvfrom(1024)
print(f"received from server : {data.decode()}")
client_socket.close()
