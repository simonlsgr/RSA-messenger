import RSA.rsa as rsa
import AES.aes as aes

keyntemp = 1727905906709714784706338886185660821489624319004546252486521182854131408326175142081155065283964279252264103247644151083170376041033786140063928678466115175854528569915314097064039396917343775112000218116052930220635874998816225153651390803092573075249639100354664945206705779738286705243578126677602991838639634011040225246154771737242342635106992300640238539502668063840304230884412268610826512661571833

class main():
    def __init__(self):
        self.rsa = rsa.rsa()
        self.aes = aes.customAES()
        self.symmetric_key = self.aes.key
        self.nonce = self.aes.nonce
    
    def encrypt(self, message: str, key_n: int, key_a: int):
        encrypted_message = self.aes.encrypt(message.encode("utf-8"))

        length_bytes_symmetric_key = len(encrypted_message["key"])
        encrypted_key = self.rsa.encrypt([int.from_bytes(encrypted_message["key"], "big")], key_n, key_a)[0]

        length_bytes_nonce = len(self.nonce)
        encrypted_nonce = self.rsa.encrypt([int.from_bytes(self.nonce, "big")], key_n, key_a)[0]

        encrypted_ciphertext_byte_length = len(encrypted_message["ciphertext"])
        tag_byte_length = len(encrypted_message["tag"])
        
        encrypted_ciphertext = int.from_bytes(encrypted_message["ciphertext"], "big")
        tag = int.from_bytes(encrypted_message["tag"], "big")
        

        return {
            "encrypted_ciphertext": encrypted_ciphertext, 
            "tag": tag,
            "encrypted_ciphertext_byte_length": encrypted_ciphertext_byte_length,
            "tag_byte_length": tag_byte_length,
            "encrypted_key": encrypted_key, 
            "encrypted_nonce": encrypted_nonce, 
            "encrypted_key_byte_length": length_bytes_symmetric_key, 
            "encrypted_nonce_byte_length": length_bytes_nonce
        }
    
    def decrypt(self, encrypted_ciphertext: int, tag: int, enrypted_ciphertext_byte_length: int, tag_byte_length, encrypted_key: int, encrypted_nonce: int, encrypted_key_byte_length: int, encrypted_nonce_byte_length: int, key_n: int):
        
        encrypted_ciphertext = encrypted_ciphertext.to_bytes(enrypted_ciphertext_byte_length, "big")
        tag = tag.to_bytes(tag_byte_length, "big")
        
        decrypted_key = self.rsa.decrypt([encrypted_key], key_n)
        decrypted_nonce = self.rsa.decrypt([encrypted_nonce], key_n)


        decrypted_key = decrypted_key[0].to_bytes(encrypted_key_byte_length, "big")
        decrypted_nonce = decrypted_nonce[0].to_bytes(encrypted_nonce_byte_length, "big")

        decrypted_message = self.aes.decrypt(encrypted_ciphertext, tag, decrypted_nonce, decrypted_key)
        
        return decrypted_message.decode("utf-8")

if __name__ == "__main__":
    
    message = "Test message Öö Ää Üü ß"
    encrypted_out = main().encrypt(message, keyntemp)
    
    

    decrypted_out = main().decrypt(encrypted_out["encrypted_ciphertext"], encrypted_out["tag"], encrypted_out["encrypted_ciphertext_byte_length"], encrypted_out["tag_byte_length"], encrypted_out["encrypted_key"], encrypted_out["encrypted_nonce"], encrypted_out["encrypted_key_byte_length"], encrypted_out["encrypted_nonce_byte_length"], keyntemp)
    decrypted_out2 = main().decrypt(1222775407911433368576202038872485028357854914267366297625024431794348722,142718865486993846770382639289126472534,30,16,1615573361252496178413435264685190470591533188665256453731200897822898074506659041918629700878857383796378909940693165968460552548778955478104562967525102249994204824177458936895749700986914205233897242319532288656608926782558052652508328071123816849218416292585999116756906368700776300025215760983983540286793312346540957014138371530740777219759150215897888082345920950648174331369509609796023999100644208,1200121382925441114196560437505711420734268181798802707696787254544910189867060723041589286501909460679072163945200171819513939098206728539208570758468291562706202714916724113288774926336875164560588577306929990223122016043155533338320964612758170362123649357709416218295328558288123598668378301492735283216305436206729912300889997102951721594861692735868650665769727258442339569201631148925383110242147209,16,16,1727905906709714784706338886185660821489624319004546252486521182854131408326175142081155065283964279252264103247644151083170376041033786140063928678466115175854528569915314097064039396917343775112000218116052930220635874998816225153651390803092573075249639100354664945206705779738286705243578126677602991838639634011040225246154771737242342635106992300640238539502668063840304230884412268610826512661571833)

    # print(decrypted_out2)
    print(encrypted_out)
