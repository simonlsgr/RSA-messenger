import random
import numpy as np

class rsa():
    def __init__(self, message):
        self.message = message
    
    def encrypt(self):
        pass
    
    def load_key(self):
        with open("backend_tests/RSA/key/private_key.json", "r") as f:
            key = f.read()
        print(key)
    
    def generate_key(self):
        pass

    def isPrimeMRT(self, p, k):
        c = 0
        while k > 0:
            if self.MillerRabinTest(p) == False:
                return False
            k -= 1
            
        return True
    

    def MillerRabinTest(self, p):
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

    

    def generatePrimeNumber(self, length):
        a = "1"
        z = "9"
        for i in range(length):
            a += "0"
            z += "9"
        while True:
            number = random.randint(int(a), int(z))
            if self.isPrimeMRT(number, 8):
                return number

    def generatePQNM(self, lowerValue, upperValue):
        p = self.generatePrimeNumber(random.randint(lowerValue, upperValue))
        q = self.generatePrimeNumber(random.randint(lowerValue, upperValue))
        n = p * q
        m = (p - 1) * (q - 1)

        return {"p": p,"q": q,"n": n,"m": m}

    def EuclideanAlgorithmIsOne(self, a, n):
        if a == 1 and n == 0:
            return True
        elif n == 0:
            return False
        return self.EuclideanAlgorithmIsOne(int(n), int(int(a) % int(n)))


    def generateCoprime(self, n):
        while True:
            a = random.randint(2, n - 1)
            if self.EuclideanAlgorithmIsOne(a, n) == True:
                return a

    def extendedEuclideanAlgorithm(self, array1, array2):
        if array2[0] == 1:
            return array2[2]
        values1 = np.array(array1)
        values2 = np.array(array2)
        factor = values1[0] // values2[0]
        values2 = np.subtract(values1, np.multiply(factor, values2))
        return self.extendedEuclideanAlgorithm(array2, values2)

    
if __name__ == "__main__":
    message = input("Message: ")
    rsa(message).load_key()