import socket
import hashlib

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 10001))


username = client.recv(1024).decode()
client.send(input(username).encode())
password = client.recv(1024).decode()
client.send(hashlib.sha256(input(password).encode()).hexdigest().encode())
print(client.recv(1024).decode())

function = client.recv(1024).decode()
client.send(input(function).encode())


print(client.recv(1024).decode())


