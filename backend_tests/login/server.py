import sqlite3
import hashlib
import socket
import threading
#import the messages.py file from the backend_tests/sending_messages folder
import backend_tests.sending_messages.messages as messages


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 10001))

server.listen()


def handle_connection(c):
    c.send("Username: ".encode())
    username = c.recv(1024).decode()
    c.send("Password: ".encode())
    password = c.recv(1024).decode()
    

    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))

    if cur.fetchall():
        c.send("Login successful".encode())
        messages.main()

    else:
        c.send("Login failed".encode())


while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()