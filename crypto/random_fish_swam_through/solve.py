import re
import random 

def LD(n):
    for i in range(2,n,1):
        if n%i==0:
            return i
    return n

def shuffle(p,k):
    ld = LD(len(p))
    random.seed(k)
    c = [p[i:i + ld] for i in range(0, len(p), ld)] 
    for i in c:
        random.shuffle(i)
    return c

def encrypt(p,k):
    new = shuffle(list(p),k)
    final =prettyRet(new)
    return final

def prettyRet(c):
    cipher = ""
    for i in c:
        cipher+="".join(i)
    return cipher

def decrypt(c,k):
    plain = unshuffle(c,k)
    return "".join(plain)

    
def unshuffle(c,k):
    total = len(c)
    p = [None]*total
    ph = list(range(total))
    key = shuffle(ph,k)
    count = 0
    for i in key:
        for x in i :
            p[int(x)]=c[count]
            count+=1
    return p

KEY = "im a fish blub"
a = open("flag.txt","r")
c = a.readline().strip()
p = decrypt(c,KEY)
print("DECRYPTED:")
print(p)
