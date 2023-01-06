import sqlite3
import socket
import threading
import datetime



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 10001))

server.listen()



def fetch_messages(username, client):
    conn = sqlite3.connect('backend_server_side/users.db')
    cur = conn.cursor()
    own_id = cur.execute("SELECT id FROM users WHERE username = ?", (username, )).fetchall()[0][0]
    
    all_messages = cur.execute("SELECT * FROM messages_RAM WHERE receiver_id = ?", (own_id, )).fetchall()
    
    for i in range(len(all_messages)):
        all_messages[i] = list(all_messages[i])
    
    for i, j in enumerate(all_messages):
        all_messages[i][1] = cur.execute("SELECT username FROM users WHERE id = ?", (all_messages[i][1], )).fetchall()[0][0]
        all_messages[i][2] = cur.execute("SELECT username FROM users WHERE id = ?", (all_messages[i][2], )).fetchall()[0][0]
    
    client.sendall(str(all_messages).encode())
    
    

    # deleting received messages from RAM
    message_ids_list = eval(client.recv(1024).decode())
    client.send("ready".encode())
    username_from_user = client.recv(1024).decode()
    client.send("ready".encode())

    user_id = cur.execute("SELECT id FROM users WHERE username = ?", (username_from_user, )).fetchall()[0][0]

    for message_id in message_ids_list:
        cur.execute("DELETE FROM messages_RAM WHERE message_id = ? AND receiver_id = ?", (message_id, user_id))
    conn.commit()

def send_message(username, client):
    conn = sqlite3.connect('backend_server_side/users.db')
    cur = conn.cursor()
    own_id = cur.execute("SELECT id FROM users WHERE username = ?", (username, )).fetchall()[0][0]
    receiver = client.recv(1024).decode()

    try:
        receiver_id = cur.execute("SELECT id FROM users WHERE username = ?", (receiver, )).fetchall()[0][0]
        client.send("receiver known".encode())
    except:
        client.send("receiver unkown".encode())
        return

    try:
        keys = cur.execute("SELECT rsa_key_n, rsa_key_a FROM users WHERE username = ?", (receiver, )).fetchall()[0]
        client.send(str(keys).encode())
    except:
        print("receiver unkown")
        client.send("receiver unkown".encode())
        
    message = eval(client.recv(4294967296).decode())
    
    date = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    
    cur.execute("INSERT INTO messages_RAM (receiver_id, sender_id, encrypted_ciphertext, tag, encrypted_ciphertext_byte_length, tag_byte_length, encrypted_symmetric_key, encrypted_nonce, encrypted_symmetric_key_byte_length, encrypted_nonce_byte_length, public_key_rsa_n, date_sent) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (receiver_id, own_id,str(message["encrypted_ciphertext"]), str(message["tag"]), str(message["encrypted_ciphertext_byte_length"]), str(message["tag_byte_length"]), str(message["encrypted_key" ]), str(message["encrypted_nonce"]), str(message["encrypted_key_byte_length"]), str(message["encrypted_nonce_byte_length"]), str(keys[0]), date))
    
    ### GENERATE NEW RSA KEY PAIR
    key_pair = client.recv(1024).decode()
    key_pair = eval(key_pair)
    key_pair = (str(key_pair[0]), str(key_pair[1]))
    cur.execute("UPDATE users SET rsa_key_n = ?, rsa_key_a = ? WHERE username = ?", (key_pair[0], key_pair[1], username))
    
    conn.commit()
    




def handle_connection(client):
    ### USER AUTHENTICATION
    client.send("Username: ".encode())
    username = client.recv(1024).decode()
    client.send("Password: ".encode())
    password = client.recv(1024).decode()

    conn = sqlite3.connect('backend_server_side/users.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))

    if cur.fetchall():
        client.send("Login successful".encode())
        
        function = client.recv(1024).decode()
        if function == "f":
            fetch_messages(username, client)
            client.send("fetching messages".encode())
        elif function == "s":
            send_message(username, client)
            client.send("sending message".encode())
        else:
            client.send("function unkown".encode())

    else:
        client.send("Login failed".encode())



while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()