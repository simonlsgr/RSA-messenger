import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()

cur.execute(""" 
CREATE TABLE IF NOT EXISTS messages_RAM (
    message_id INTEGER PRIMARY KEY AUTOINCREMENT,
    message VARCHAR(1) NOT NULL,
    receiver_id INTEGER NOT NULL,
    sender_id INTEGER NOT NULL,
    public_key_rsa VARCHAR(255) NOT NULL,
    date_sent DATETIME NOT NULL,
    FOREIGN KEY (receiver_id) REFERENCES users(id),
    FOREIGN KEY (sender_id) REFERENCES users(id)
)
""")

cur.execute("INSERT INTO messages_RAM (message, receiver_id, sender_id, public_key_rsa, date_sent) VALUES (?, ?, ?, ?, ?)", ("Hello", 1, 2, "55 , 7", "1970-01-01 00:00:00"))
conn.commit()