import socket
import hashlib
import sys
sys.path.append("backend_tests")
import backend_main as backend_main
sys.path.append("backend_tests/login")


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
    list_of_tuples_containing_fetched_messages = eval(fetched_messages)
    list_encrypted_messages = []
    for i, j in enumerate(list_of_tuples_containing_fetched_messages):
        for k, l in enumerate(j):
            print(i, l)



client.send("".encode())

