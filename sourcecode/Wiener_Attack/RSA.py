import numpy as np
import random
import time
from gmpy2 import *
# import generate_prime

random.seed(time.time())

class RSA(object):
    def __init__(self, bit, bit_d = 0):
        p, q = gen_prime( div(bit, 2) ), gen_prime( bit*2 )
        self.n = mul(p, q)
        p_q = mul(p-1, q-1)
        self.d = random.randint(1<< bit, 1<< (bit+1)) |1    if bit_d == 0 else random.randint(1<< bit_d, 1<< (bit_d+1)) |1

        while ( gcd(p_q, self.d) != 1):
            self.d = random.randint(1<< bit, 1<< (bit+1)) |1    if bit_d == 0 else random.randint(1<< bit_d, 1<< (bit_d+1)) |1

        self.e = invert(self.d, p_q)
        print('n = %d'  %(self.n))
        print('e = %d'  %(self.e))
        print('d = %d'  %(self.d))
        print()
        # print('d = %d'  %(self.d))

    def encode(self, message):
        c = pow(message, self.e, self.n)
        return c

    def decode(self, cipher):
        d = pow(cipher, self.d, self.n)
        return d

    
if __name__ == '__main__':
    time_0 = time.time()
    bit = 2048      
    rsa = RSA(bit, 512)

    time_1 = time.time()
    mess = random.randint(1<< bit, 1<< (bit+1))
    print('\nmessage = %d'  %(mess) )

    cipher = rsa.encode( message = mess)
    print( 'cipher = %d'  %(cipher) )

    time_2 = time.time()
    print( 'decode  = %d'  %(rsa.decode(cipher = cipher)) )

    time_3 = time.time()

    print('\nthời gian sinh khóa: %f' %(time_1 - time_0) )
    print('thời gian mã hóa: %f' %(time_2 - time_1) )
    print('thời gian giải mã: %f' %(time_3 - time_2))
