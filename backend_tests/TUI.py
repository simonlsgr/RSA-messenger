import socket
import hashlib

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 10001))

message = client.recv(1024).decode()
client.send(input(message).encode())
message = client.recv(1024).decode()
client.send(hashlib.sha256(input(message).encode()).hexdigest().encode())
print(client.recv(1024).decode())

