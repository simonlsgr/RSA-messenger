from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class customAES:
    def __init__(self):
        self.key = get_random_bytes(16)
        self.cipher = AES.new(self.key, AES.MODE_EAX)
        self.nonce = self.cipher.nonce

    def encrypt(self, message):
        ciphertext, tag = self.cipher.encrypt_and_digest(message)
        return {"ciphertext": ciphertext, "tag": tag, "nonce": self.nonce, "key": self.key}

    def decrypt(self, ciphertext, tag, nonce, key):
        cipher_decrypt = AES.new(key, AES.MODE_EAX, nonce)
        plaintext = cipher_decrypt.decrypt(ciphertext)
        try:
            cipher_decrypt.verify(tag)
            return plaintext
        except ValueError:
            return "Key incorrect or message corrupted".encode("utf-8")

if __name__ == "__main__":
    message = "Test Message".encode("utf-8")
    decryption_info = customAES().encrypt(message)
    print(decryption_info)
    encryption_info = customAES().decrypt(decryption_info["ciphertext"], decryption_info["tag"], decryption_info["nonce"], decryption_info["key"])
    print(encryption_info)
    
    