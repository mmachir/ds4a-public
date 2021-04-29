# coding: utf-8

# Decrypt using a private key

def private_key(p,q,e):
    d = (2*(p-1)*(q-1)+1)/e
    return d

def decrypt(ec):
    p = 523
    q = 541
    n = p*q
    e = 11
    d= private_key(p,q,e)
    if d.is_integer():
        d = int(d)
    else:
        exit('Check that p and q values are valid primes producing an integer private key.')
    lets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
    nums = list(range(1,28))
    decode = dict(zip(nums, lets))
    c = decode[(ec**d)%n]
    return c

def main():
    encstr = input('Cipher to decrypt: ')
    enclst = list(map(int,encstr.split(' ')))
    cstr = ''
    for ec in enclst:
        c = decrypt(int(ec))
        cstr += c
    print(f'DECRYPTED MESSAGE:\n{cstr}')

if(__name__ == '__main__'):
    main()
