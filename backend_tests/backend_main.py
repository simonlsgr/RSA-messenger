import RSA.rsa as rsa
import AES.aes as aes

keyntemp = 1727905906709714784706338886185660821489624319004546252486521182854131408326175142081155065283964279252264103247644151083170376041033786140063928678466115175854528569915314097064039396917343775112000218116052930220635874998816225153651390803092573075249639100354664945206705779738286705243578126677602991838639634011040225246154771737242342635106992300640238539502668063840304230884412268610826512661571833

class main():
    def __init__(self):
        self.rsa = rsa.rsa()
        self.aes = aes.customAES()
        self.symmetric_key = self.aes.key
        self.nonce = self.aes.nonce
    
    def encrypt(self, message: str):
        encrypted_message = self.aes.encrypt(message.encode("utf-8"))

        length_bytes_symmetric_key = len(encrypted_message["key"])
        encrypted_key = self.rsa.encrypt([int.from_bytes(encrypted_message["key"], "big")], keyntemp)[0]

        length_bytes_nonce = len(self.nonce)
        encrypted_nonce = self.rsa.encrypt([int.from_bytes(self.nonce, "big")], keyntemp)[0]


        return {
            "encrypted_ciphertext": encrypted_message["ciphertext"], 
            "tag": encrypted_message["tag"] , 
            "encrypted_key": encrypted_key, 
            "encrypted_nonce": encrypted_nonce, 
            "encrypted_key_byte_length": length_bytes_symmetric_key, 
            "encrypted_nonce_byte_length": length_bytes_nonce}
    
    def decrypt(self, encrypted_ciphertext: bytes, tag: bytes, encrypted_key: int, encrypted_nonce: int, encrypted_key_byte_length: int, encrypted_nonce_byte_length: int):
        
        
        
        decrypted_key = self.rsa.decrypt([encrypted_key], keyntemp)
        decrypted_nonce = self.rsa.decrypt([encrypted_nonce], keyntemp)


        decrypted_key = decrypted_key[0].to_bytes(encrypted_key_byte_length, "big")
        decrypted_nonce = decrypted_nonce[0].to_bytes(encrypted_nonce_byte_length, "big")
        decrypted_message = self.aes.decrypt(encrypted_ciphertext, tag, decrypted_nonce, decrypted_key)
        return {"decrypted_message": decrypted_message, "decrypted_key": decrypted_key, "decrypted_nonce": decrypted_nonce, "tag": tag}

if __name__ == "__main__":
    
    message = "Test Message"
    encrypted_out = main().encrypt(message)

    decrypted_out = main().decrypt(encrypted_out["encrypted_ciphertext"], encrypted_out["tag"], encrypted_out["encrypted_key"], encrypted_out["encrypted_nonce"], encrypted_out["encrypted_key_byte_length"], encrypted_out["encrypted_nonce_byte_length"])
    
    print(decrypted_out["decrypted_message"].decode("utf-8"))
