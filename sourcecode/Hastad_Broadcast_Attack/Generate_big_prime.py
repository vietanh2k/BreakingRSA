import random
import time
from gmpy2 import *

random.seed(time.time())

def gen_prime(bit):   # nhập vào số bit
    num_prime = random.randint(1<< bit, 1<< (bit+1)) | 1
    while is_prime(num_prime) == False:
        num_prime = random.randint(1<< bit, 1<< (bit+1)) | 1

    return num_prime


start_time = time.time()
print(gen_prime(3072))

end_time = time.time()
print('thời gian chạy chương trình: ', end_time - start_time)
