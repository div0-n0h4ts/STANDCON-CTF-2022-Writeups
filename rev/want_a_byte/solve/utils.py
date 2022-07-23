import hashlib
from string import printable
key_space = printable

def patch_keyspace():
    global key_space
    key_space = 'a' * len(key_space)


def generate_mask(inp):
    mod_inp = (lambda x: x.split()[0])(inp)
    _mod_inp = ''
    for i in mod_inp:
        _mod_inp += chr((ord(i) ^ 10 + ord(i)) * 3 % 120 + 5)

    mod_inp_ = hashlib.md5(_mod_inp.encode('utf-8')).hexdigest()
    return mod_inp
