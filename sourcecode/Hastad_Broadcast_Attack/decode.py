# from crt import *
# import RSA

random.seed(time.time())
e = 97
bit = 1024
mess = random.randint(1<< bit, 1<< (bit+1))
print("mess  : %d" %(mess))

ciphers = ()
n = ()
for i in range(e):
    rsa = RSA(bit, default_e= e)      # e = 7
    n_, c = rsa.n,  rsa.encode( message = mess)
    ciphers = ciphers + (c,)
    n = n + (n_,)

M = crt(ciphers, n)
m = int(iroot(M, e)[0])     # m^e  = M
print("decode: %d" %(m))
