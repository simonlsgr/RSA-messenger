import sqlite3
import hashlib

conn = sqlite3.connect('backend_server_side/users.db')
cur = conn.cursor()

cur.execute(""" 
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255) NOT NULL UNIQUE,
    display_name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

def create_user(username, display_name, password):
    password1 = hashlib.sha256(password.encode()).hexdigest()
    
    try:
        cur.execute("INSERT INTO users (username, display_name, password) VALUES (?, ?, ?)", (username, display_name, password1))
        return "User {} created!".format(username)
    except sqlite3.IntegrityError:
        return "Username already exists!"


print(create_user("root", "root", "root"))
print(create_user("Paul", "Paul", "Paul1234"))
print(create_user("RKores", "RKores", "RKores2023!"))

conn.commit()