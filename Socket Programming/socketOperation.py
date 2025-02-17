import socket

def calculate(operation, num1, num2):
    """Perform the requested operation."""
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        return "Error: Invalid operation"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))  # Bind to localhost
server_socket.listen(1)  # Listen for 1 connection

print("Server is running and waiting for connections...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connected to {addr}")

    data = client_socket.recv(1024).decode()  # Receive data from client
    operation, num1, num2 = data.split()  # Split the received string
    num1, num2 = float(num1), float(num2)  # Convert to numbers

    result = calculate(operation, num1, num2)  # Perform the operation

    client_socket.send(str(result).encode())  # Send result back to client
    client_socket.close()  # Close the client connection


import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))  # Connect to the server

# Take user input
operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
num1 = input("Enter first number: ").strip()
num2 = input("Enter second number: ").strip()

client_socket.send(f"{operation} {num1} {num2}".encode())  # Send data to server

result = client_socket.recv(1024).decode()  # Receive result from server
print(f"Result from server: {result}")

client_socket.close()  # Close the connection
