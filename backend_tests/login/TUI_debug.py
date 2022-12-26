import socket
import hashlib

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 10001))

username_in = "Paul"
password_in = "Paul1234"
option = "f"


username = client.recv(1024).decode()
client.send(username_in.encode())
password = client.recv(1024).decode()
client.send(hashlib.sha256(password_in.encode()).hexdigest().encode())
client.recv(1024)
if option == "f":
    client.send("f".encode())

    print(client.recv(1024).decode())
    fetched_messages = client.recv(4294967296).decode()
    print(eval(fetched_messages))

client.send("".encode())

