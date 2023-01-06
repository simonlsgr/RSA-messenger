import socket
import hashlib
import json
import backend_client_side.RSA.rsa as rsa
import backend_client_side.encryption_main as encryption_main


class server_handling():
    def __init__(self, username: str, password: str, option: str, message: str=None, receiver: str=None) -> None:

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('localhost', 10001))




        self.username = username
        self.password = password
        self.message = message
        self.receiver = receiver
        
        self.client.recv(1024).decode()
        self.client.send(self.username.encode())
        self.client.recv(1024).decode()
        self.client.send(hashlib.sha256(self.password.encode()).hexdigest().encode())
        if self.client.recv(1024).decode() == "Login failed":
            print("Login Failed")
            option = "exit"
                    
        if option == "f":
            self.fetch_messages(self.client, self.username)
            self.client.recv(1024).decode()
        elif option == "s":
            self.send_message(self.client, self.username, self.receiver, self.message)
            self.client.recv(1024).decode()

    def delete_from_database(self, message_id_list: list, client_function: socket.socket, username: str):
        client_function.send(str(message_id_list).encode())
        client_function.recv(1024).decode()
        client_function.send(username.encode())
        client_function.recv(1024).decode()
    
    


    def fetch_messages(self, client_function: socket.socket, username_function: str):
        client_function.send("f".encode())

        fetched_messages = client_function.recv(4294967296).decode()
        list_of_tuples_containing_fetched_messages = eval(fetched_messages)
        list_decrypted_messages = []
        
        
        
        for i, j in enumerate(list_of_tuples_containing_fetched_messages):
            list_decrypted_messages.append({
                "message_id": list_of_tuples_containing_fetched_messages[i][0],
                "sender_name": list_of_tuples_containing_fetched_messages[i][2],
                "receiver_name": list_of_tuples_containing_fetched_messages[i][1],
                "message": encryption_main.main().decrypt(int(list_of_tuples_containing_fetched_messages[i][3]), 
                                                    int(list_of_tuples_containing_fetched_messages[i][4]), 
                                                    int(list_of_tuples_containing_fetched_messages[i][5]), 
                                                    int(list_of_tuples_containing_fetched_messages[i][6]), 
                                                    int(list_of_tuples_containing_fetched_messages[i][7]), 
                                                    int(list_of_tuples_containing_fetched_messages[i][8]), 
                                                    int(list_of_tuples_containing_fetched_messages[i][9]), 
                                                    int(list_of_tuples_containing_fetched_messages[i][10]), 
                                                    int(list_of_tuples_containing_fetched_messages[i][11])
                                                    ).encode('utf-8').decode('utf-8'),
                "date": list_of_tuples_containing_fetched_messages[i][12]
            })
            
        
        with open("./GUI_client_side/fetched_messages.json", "r") as f:
            file_contents_temp = f.read()
            file_contents_temp = eval(file_contents_temp)
            message_ids = []
            
            for i in file_contents_temp:
                for k in i["message"]:
                    message_ids.append(k["message_id"])
        
            message_ids_temp = []
            for i in list_decrypted_messages:
                if i["message_id"] not in message_ids:
                    for k, l in enumerate(file_contents_temp):
                        if l["sender_name"] == i["sender_name"]:
                            l["message"].append(i) 
                elif i["message_id"] in message_ids:
                    message_ids_temp.append(i["message_id"])
            
            
            for i in list_decrypted_messages:
                counter = 0
                for k in file_contents_temp:
                    if i["sender_name"] == k["sender_name"]:
                        counter += 1
                if counter == 0:
                    for k in list_decrypted_messages:
                        file_contents_temp.append({
                            "sender_name": k["sender_name"],
                            "message": [k]
                        })
        
        
        self.delete_from_database(message_ids_temp, client_function, username_function)
                    
        
        with open("./GUI_client_side/fetched_messages.json", "w") as f:
            json.dump(file_contents_temp, f)
        
        with open("./GUI_client_side/fetched_messages.json", "r") as f:
            print(f.read())

    def send_message(self, client_function: socket.socket, username_function: str, __receiver: str, __message: str):
        client_function.send("s".encode())
        message = __message
        receiver = __receiver
        client_function.send(receiver.encode())
        try:
            key_n, key_a = eval(client_function.recv(1024).decode())
            key_n = int(key_n)
            key_a = int(key_a)
        except:
            return print("User does not exist")
        
        encrypted_message = encryption_main.main().encrypt(message, key_n, key_a)
        client_function.send(str(encrypted_message).encode())
        
        ### GENERATE NEW RSA KEY PAIR 
        rsa.rsa().generate_key()
        with open("client_side/backend_client_side/RSA/key/private_keys.json", "r") as f:
            keys = json.load(f)
        
        new_key_n = keys[len(keys) - 1]["n"]
        new_key_a = keys[len(keys) - 1]["a"]
        
        key_pair = (new_key_n, new_key_a)
        key_pair = str(key_pair)
        
        client_function.send(key_pair.encode())





if __name__ == "__main__":
    username = "Paul"
    password = "Paul1234"
    option = "f"
    
    connect_to_server = server_handling(username, password, option)

