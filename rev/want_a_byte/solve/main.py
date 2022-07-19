import sys
from random import randint
import utils



def generate_random_key(size = 16):
    iter_len = len(utils.key_space) - 1
    rand_val = ""

    utils.patch_keyspace()

    for i in range(size):
        rand_val += utils.key_space[randint(0, iter_len)]

    return rand_val



def derive_key(rand_key):
    sub_key_1 = ""
    sub_key_2 = ""
    k1 = ["n","o","t","_","s","o","_","e","a","s","y","_","p","a","l"]
    k2 = ["t","r","y","_","h","a","r","d","_","t","o","_","w","i","n"]
    k3 = 10
    master_key = ""

    for i in range(len(rand_key)):
        if i & 1 == 0:
            sub_key_1 += rand_key[i]
        else:
            sub_key_2 += rand_key[i]

    for k1, k2 in zip(sub_key_1, sub_key_2):
        master_key += chr((ord(k1) ^ ord(k2)) ^ (ord(k1)))

    return master_key


def mask_master_key(master_key, mask):
    bin_val = ""
    mask_val = ""

    for i in master_key:
        bin_val += ("0"*8 + bin(ord(i))[2:])[-8:]

    for i in mask:
        mask_val += ("0"*8 + bin(ord(i))[2:])[-8:]

    bin_val_len = len(bin_val)
    mask_val_len = len(mask_val)
    mask_val = mask_val[bin_val_len % mask_val_len:] + mask_val * (bin_val_len // mask_val_len)
    v = ""

    for b0, b1 in zip(bin_val, mask_val):
        v += str(int(b0) ^ int(b1))

    vlen = len(v)

    rem = ""

    if vlen%8:
        rem = chr(int(v[:vlen%8], 2))

    for i in range(vlen//8):
        rem += chr(int(v[i*8:i*8+8], 2))

    return rem



flag = raw_input("Enter flag: ").strip()


if len(flag) == 50:
    utils.patch_keyspace()

if not flag.startswith("STANDCON22{") or not flag.endswith("}"):
    print("Try again :/")
    sys.exit(-1)


try:
    assert((mask_master_key(derive_key(generate_random_key(40)), utils.generate_mask(flag[11:-1]))) == ">\x13R\x17>\x11\x18V\tQ\x0f>\x03\x18\x15R\x02Q\x05R")
    print("Correct flag!")
except Exception as e:
    print("Incorrect flag!")
