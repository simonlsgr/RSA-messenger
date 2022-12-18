import RSA.rsa as rsa
import AES.aes as aes

keyntemp = 55

class main():
    def __init__(self):
        self.rsa = rsa.rsa()
        self.aes = aes.customAES()
        self.symmetric_key = self.aes.key
        self.nonce = self.aes.nonce
    
    def encrypt(self, message):
        encrypted_message = self.aes.encrypt(message.encode("utf-8"))
        encrypted_key = self.rsa.encrypt(self.symmetric_key, keyntemp)
        encrypted_nonce = self.rsa.encrypt(self.nonce, keyntemp)
        return {"encrypted_message": encrypted_message, "encrypted_key": encrypted_key, "encrypted_nonce": encrypted_nonce}
    
    def decrypt(self, encrypted_message, encrypted_key, encrypted_nonce):
        decrypted_message = self.aes.decrypt(encrypted_message["ciphertext"], encrypted_message["tag"]).decode("utf-8")
        decrypted_key = self.rsa.decrypt(encrypted_key, keyntemp)
        decrypted_nonce = self.rsa.decrypt(encrypted_nonce, keyntemp)
        return {"decrypted_message": decrypted_message, "decrypted_key": decrypted_key, "decrypted_nonce": decrypted_nonce}

if __name__ == "__main__":
    message = input("Message: ")
    main = main()
    encrypted_out = main.encrypt(message)
    print(encrypted_out)
    decrypted_out = main.decrypt(encrypted_out["encrypted_message"], encrypted_out["encrypted_key"], encrypted_out["encrypted_nonce"])
    print(decrypted_out)
