import backend_tests.RSA.rsa as rsa

class main:
    def __init__(self, message, sender, receiver, key_a):
        self.message = message
        self.sender = sender
        self.receiver = receiver
        self.key_a = key_a

    def send(self):
        self.key_a
        return 
    
    def encrypt(self):
        rsa.encrypt(self.message, self.key_a)

if __name__ == "__main__":
    message = input("Message: ")
    sender = int(input("Sender: "))
    receiver = int(input("Receiver: "))
    key = input("Key: ")
    main(message, sender, receiver, key).send()