import socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1",12346))
server_socket.listen(5)
print("Server is listening ")
conn,addr=server_socket.accept()
print(f"Connected to {addr}")
while True:
    word=conn.recv(1024).decode()
    if not word:
        break
    reversed=word[::-1]
    conn.send(reversed.encode())
conn.close()
server_socket.close()

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12346))
while True:
    word = input("Enter a word (or type 'exit' to quit): ")
    if word.lower() == 'exit':
        break
    client_socket.send(word.encode())
    reversed_word = client_socket.recv(1024).decode()
    print("Reversed word from server:", reversed_word)
client_socket.close() 
