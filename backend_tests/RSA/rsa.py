import random
import numpy as np
import json

class rsa():
    def __init__(self, message):
        try:
            self.message = int(message)
        except:
            self.message = message
    
    def encrypt(self, message):
        key = self.load_key()
        message_encrypted = []
        message_buffer = str(self.message)
        for i in message_buffer:
            message_encrypted.append(pow(int(i), key["a"], key["n"]))
        return message_encrypted

    def decrypt(self):
        key = self.load_key()
        message_decrypted = []
        b = self.extended_euclidean_algorithm([key["m"], 1, 0], [key["a"] , 0, 1])
        for i in self.message:
            message_decrypted.append(pow(int(i), b, key["n"]))
        
        try:
            return int("".join(map(str, message_decrypted)))
        except:
            return message_decrypted
        
    
    def load_key(self):
        key = ""
        with open("backend_tests/RSA/key/private_key.json", "r") as f:
            key = f.read()
        key = json.loads(key)
        return key
    
    def generate_key(self):
        dict = self.generate_p_q_n_m(10, 20)
        dict["a"] = self.generate_coprime(dict["m"])
        with open("backend_tests/RSA/key/private_key.json", "w") as f:
            json.dump(dict, f)

    
    
    def is_prime_MRT(self, p, k):
        c = 0
        while k > 0:
            if self.Miller_Rabin_test(p) == False:
                return False
            k -= 1
            
        return True
    
    def Miller_Rabin_test(self, p):
            d = p - 1
            r = 0

            while d % 2 == 0:
                d //= 2
                r += 1
            a = random.randint(2, p - 1)

            x = pow(a, d, p)

            if x == 1 or x == p - 1:
                return True
            while r > 1:
                x = pow(x, 2, p)
                if x == 1:
                    return False
                if x == p - 1:
                    return True
                r -= 1
            return False

    

    def generate_prime_number(self, length):
        a = "1"
        z = "9"
        for i in range(length):
            a += "0"
            z += "9"
        while True:
            number = random.randint(int(a), int(z))
            if self.is_prime_MRT(number, 8):
                return number

    def generate_p_q_n_m(self, lowerValue, upperValue):
        p = self.generate_prime_number(random.randint(lowerValue, upperValue))
        q = self.generate_prime_number(random.randint(lowerValue, upperValue))
        n = p * q
        m = (p - 1) * (q - 1)

        return {"p": p,"q": q,"n": n,"m": m}

    def euclidean_algorithm_is_one(self, a, n):
        if a == 1 and n == 0:
            return True
        elif n == 0:
            return False
        return self.euclidean_algorithm_is_one(int(n), int(int(a) % int(n)))


    def generate_coprime(self, n):
        while True:
            a = random.randint(2, n - 1)
            if self.euclidean_algorithm_is_one(a, n) == True:
                return a

    def extended_euclidean_algorithm(self, array1, array2):
        if array2[0] == 1:
            return int(array2[2])
        values1 = np.array(array1)
        values2 = np.array(array2)
        factor = values1[0] // values2[0]
        values2 = np.subtract(values1, np.multiply(factor, values2))
        return self.extended_euclidean_algorithm(array2, values2)
    

    
if __name__ == "__main__":
    message = int(input("Message: "))
    # rsa(message).generate_key()
    # rsa(message).load_key()
    y = rsa(message).encrypt(message)
    x = rsa(y).decrypt()
    print(y, x)