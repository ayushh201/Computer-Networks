import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('127.0.0.1',12347)
message = "networks"
client_socket.sendto(message.encode(),server_address)
data,_ = client_socket.recvfrom(1024)
print(f"received from server : {data.decode()}")
client_socket.close()


import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ("127.0.0.1",12347)
server_socket.bind(server_address)
print("server is listening on port 12347")
while True:
    data,client_address = server_socket.recvfrom(1024)
    print(f"data received from client {client_address} , data : {data.decode()}")
    modified_data = data.decode()[::-1].swapcase()
    server_socket.sendto(modified_data.encode(),client_address)
