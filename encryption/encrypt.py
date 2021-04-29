# coding: utf-8

# Encrypt using a public key  

def encrypt(c):
    p = 523
    q = 541
    n = p*q
    e = 11
    # public key = n, e
    lets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
    nums = list(range(1,28))
    encode = dict(zip(lets, nums))
    ec = (encode[c]**e)%n
    return ec

def main():
    origstr = input('String to encrypt: ')
    enc = []
    for c in origstr.upper():
        en = encrypt(c)
        enc.append(str(en))
    encstr = " ".join(enc)
    print(f"CIPHER:\n{encstr}")

if(__name__ == '__main__'):
    main()
