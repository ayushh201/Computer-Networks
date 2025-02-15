#server
import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12347))
server_socket.listen(1)
print("Server is listening on port 12347")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")
data = conn.recv(1024).decode()
num1, num2 = map(int, data.split())
result = num1 + num2
conn.send(str(result).encode())
conn.close()
server_socket.close()

#client
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12347))
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
client_socket.send(f"{num1} {num2}".encode())
result = client_socket.recv(1024).decode()
print(f"Sum received from server: {result}")
client_socket.close()
