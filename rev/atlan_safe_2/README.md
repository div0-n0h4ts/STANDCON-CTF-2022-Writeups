# AtlanSafe2 Write-Up


file 

```
file atlansafe2.exe
enc.exe: PE32+ executable (console) x86-64, for MS Windows
```

running strings + grep to find what dlls it’s used

```
blibcrypto-1_1.dll
blibffi-7.dll
blibssl-1_1.dll
bpython310.dll
bucrtbase.dll
6python310.dll
```

we can see crypto, python310

python3 -> we can use pyinstrxtractor

[https://github.com/extremecoders-re/pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor)

running this to extract the application, would extract it including the  atlansafe2.pyc file

```
python3 pyinstxtractor.py atlansafe2.exe
[+] Processing atlansafe2.exe
[+] Pyinstaller version: 2.1+
[+] Python version: 310
[+] Length of package: 8631277 bytes
[+] Found 109 files in CArchive
[+] Beginning extraction...please standby
[+] Possible entry point: pyiboot01_bootstrap.pyc
[+] Possible entry point: pyi_rth_subprocess.pyc
[+] Possible entry point: pyi_rth_inspect.pyc
[+] Possible entry point: pyi_rth_pkgutil.pyc
[+] Possible entry point: pyi_rth_multiprocessing.pyc
[+] Possible entry point: atlansafe2.pyc
[!] Warning: This script is running in a different Python version than the one used to build the executable.
[!] Please run this script in Python310 to prevent extraction errors during unmarshalling
[!] Skipping pyz extraction
[+] Successfully extracted pyinstaller archive: atlansafe2.exe

You can now use a python decompiler on the pyc files within the extracted directory
```

it’s the latest python version, so uncompyle6 or decompyle3 wont work for this pyc file.

 xxd on atlansafe2.pyc file

```
00000000: 610d 0d0a 0000 0000 0000 0000 0000 0000  a...............
00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
00000020: 0002 0000 0040 0000 0073 4200 0000 6400  .....@...sB...d.
00000030: 6401 6c00 6d01 5a01 0100 6400 6402 6c02  d.l.m.Z...d.d.l.
00000040: 5a02 6400 6403 6c03 6d04 5a04 0100 6404  Z.d.d.l.m.Z...d.
00000050: 6405 8400 5a05 6406 6407 8400 5a06 6408  d...Z.d.d...Z.d.
00000060: 6409 8400 5a07 6507 8300 0100 6402 5300  d...Z.e.....d.S.
00000070: 290a e900 0000 0029 01da 0341 4553 4e29  )......)...AESN)
00000080: 01da 0573 6c65 6570 6302 0000 0000 0000  ...sleepc.......
00000090: 0000 0000 0004 0000 0004 0000 0043 0000  .............C..
000000a0: 0073 2200 0000 7400 a001 7c01 7400 6a02  .s"...t...|.t.j.
000000b0: a102 7d02 7c02 a003 7c00 a101 7d03 7c03  ..}.|...|...}.|.
000000c0: a004 6401 a101 5300 2902 4efa 0575 7466  ..d...S.).N..utf
000000d0: 2d38 2905 7202 0000 00da 036e 6577 da08  -8).r......new..
000000e0: 4d4f 4445 5f45 4342 da07 6465 6372 7970  MODE_ECB..decryp
000000f0: 74da 0664 6563 6f64 6529 04da 0374 7874  t..decode)...txt
00000100: da03 7073 77da 0361 6573 da05 7074 6578  ..psw..aes..ptex
00000110: 74a9 0072 0d00 0000 fa0e 6174 6c61 6e73  t..r......atlans
00000120: 6166 6532 2e65 7865 da03 6465 6309 0000  afe2.exe..dec...
00000130: 0073 0600 0000 0e01 0a01 0a01 720f 0000  .s..........r...
00000140: 0063 0100 0000 0000 0000 0000 0000 0800  .c..............
00000150: 0000 0300 0000 4300 0000 737a 0000 0064  ......C...sz...d
00000160: 017d 0164 027d 0274 0064 0383 0101 0074  .}.d.}.t.d.....t
00000170: 0164 0483 0101 007c 0064 0064 0585 0219  .d.....|.d.d....
00000180: 00a0 0264 06a1 017d 0364 077d 0474 037c  ...d...}.d.}.t.|
00000190: 047c 0383 027d 057c 0064 0564 0085 0219  .|...}.|.d.d....
000001a0: 00a0 0264 06a1 017d 0364 087d 0474 037c  ...d...}.d.}.t.|
000001b0: 047c 0383 027d 067c 057c 0617 007d 0774  .|...}.|.|...}.t
000001c0: 007c 017c 0717 007c 0217 0083 0101 0074  .|.|...|.......t
000001d0: 0483 0001 0064 0053 0029 094e 7a0b 5354  .....d.S.).Nz.ST
000001e0: 414e 4443 4f4e 3232 7bfa 017d 7a10 5b21  ANDCON22{..}z.[!
000001f0: 5d20 6465 6372 7970 7469 6e67 2e2e e903  ] decrypting....
00000200: 0000 00e9 1000 0000 7204 0000 0073 1000  ........r....s..
00000210: 0000 481d 342d 506a 5ae5 43a1 feb1 d8a0  ..H.4-PjZ.C.....
00000220: fc7b 7310 0000 002b 5784 a814 10ac 0839  .{s....+W......9
00000230: 8e30 6657 7f45 3929 05da 0570 7269 6e74  .0fW.E9)...print
00000240: 7203 0000 00da 0665 6e63 6f64 6572 0f00  r......encoder..
00000250: 0000 da04 6578 6974 2908 da04 6861 7368  ....exit)...hash
00000260: da01 69da 0165 720a 0000 0072 0900 0000  ..i..er....r....
00000270: da04 7072 7431 da04 7072 7432 da02 6666  ..prt1..prt2..ff
00000280: 720d 0000 0072 0d00 0000 720e 0000 00da  r....r....r.....
00000290: 0466 6c61 6710 0000 0073 1a00 0000 0401  .flag....s......
000002a0: 0401 0801 0801 1202 0401 0a01 1202 0401  ................
000002b0: 0a01 0802 1001 0a01 721c 0000 0063 0000  ........r....c..
000002c0: 0000 0000 0000 0000 0000 0200 0000 0500  ................
000002d0: 0000 4300 0000 73ac 0000 0009 0074 0064  ..C...s......t.d
000002e0: 0283 017d 0074 01a0 027c 00a0 0364 03a1  ...}.t...|...d..
000002f0: 01a1 01a0 04a1 007d 017c 0164 0064 0485  .......}.|.d.d..
00000300: 0219 0064 056b 0272 547c 0164 0464 0685  ...d.k.rT|.d.d..
00000310: 0219 0064 076b 0272 547c 0164 0664 0885  ...d.k.rT|.d.d..
00000320: 0219 0064 096b 0272 547c 0164 0864 0a85  ...d.k.rT|.d.d..
00000330: 0219 0064 0b6b 0272 547c 0164 0a64 0c85  ...d.k.rT|.d.d..
00000340: 0219 0064 0d6b 0272 547c 0164 0c64 0e85  ...d.k.rT|.d.d..
00000350: 0219 0064 0f6b 0272 547c 0164 0e64 1085  ...d.k.rT|.d.d..
00000360: 0219 0064 116b 0272 547c 0164 1064 1285  ...d.k.rT|.d.d..
00000370: 0219 0064 136b 0272 5474 057c 0183 0101  ...d.k.rTt.|....
00000380: 006e 0109 0071 0129 144e e901 0000 007a  .n...q.).N.....z
00000390: 0b70 6173 7377 6f72 6420 3a20 7204 0000  .password : r...
000003a0: 00e9 0400 0000 da04 3037 6231 e908 0000  ........07b1....
000003b0: 00da 0439 6561 32e9 0c00 0000 da04 6234  ...9ea2.......b4
000003c0: 6638 7212 0000 00da 0434 3366 39e9 1400  f8r......43f9...
000003d0: 0000 da04 6464 3864 e918 0000 00da 0466  ....dd8d.......f
000003e0: 3536 36e9 1c00 0000 da04 3362 3737 e920  566.......3b77.
000003f0: 0000 00da 0463 3461 6329 06da 0569 6e70  .....c4ac)...inp
00000400: 7574 da07 6861 7368 6c69 62da 036d 6435  ut..hashlib..md5
00000410: 7214 0000 00da 0968 6578 6469 6765 7374  r......hexdigest
00000420: 721c 0000 0029 02da 0370 7764 7216 0000  r....)...pwdr...
00000430: 0072 0d00 0000 720d 0000 0072 0e00 0000  .r....r....r....
00000440: da04 6d61 696e 2200 0000 730e 0000 0002  ..main"...s.....
00000450: 0108 0114 0180 010a 0102 0202 fa72 3200  .............r2.
00000460: 0000 2908 da0d 4372 7970 746f 2e43 6970  ..)...Crypto.Cip
00000470: 6865 7272 0200 0000 722e 0000 00da 0474  herr....r......t
00000480: 696d 6572 0300 0000 720f 0000 0072 1c00  imer....r....r..
00000490: 0000 7232 0000 0072 0d00 0000 720d 0000  ..r2...r....r...
000004a0: 0072 0d00 0000 720e 0000 00da 083c 6d6f  .r....r......<mo
000004b0: 6475 6c65 3e01 0000 0073 0e00 0000 0c00  dule>....s......
000004c0: 0801 0c01 0806 0807 0812 0a08            ............
```

The program validates the password.
There are some interesting parts here.  We can see “aes” and “MODE_ECB” which means there’s some encryption going on here.

running strings.

```
AESN)
sleepc
utf-8)
MODE_ECB
decrypt
decode)
ptext
atlansafe2.exe
dec
)       Nz
STANDCON22{
[!] decrypting..
4-PjZ
printr
encoder
exit)
hash
prt1
prt2
flag
password : r
07b1
9ea2
b4f8r
43f9
dd8d
f566
3b77
c4ac)
input
hashlib
md5r
        hexdigestr
pwdr
main"
Crypto.Cipherr
timer
<module>
```

password  ??
under the "password" we can some sets of characters in 9 lines.

```
password : r
07b1
9ea2
b4f8r
43f9
dd8d
f566
3b77
c4ac)
```

almost every set has 4 characters only one have excess "r"  and one have a closing bracket. If we remove them for now.
we get

```
07b1
9ea2
b4f8
43f9
dd8d
f566
3b77
c4ac
```

```
07b19ea2b4f843f9dd8df5663b77c4ac
```

It has 32  characters.

checking it with hashid

```
hashid 07b19ea2b4f843f9dd8df5663b77c4ac
Analyzing '07b19ea2b4f843f9dd8df5663b77c4ac'
[+] MD2
[+] MD5
[+] MD4
[+] Double MD5
[+] LM
[+] RIPEMD-128
[+] Haval-128
[+] Tiger-128
[+] Skein-256(128)
[+] Skein-512(128)
[+] Lotus Notes/Domino 5
[+] Skype
[+] Snefru-128
[+] NTLM
[+] Domain Cached Credentials
[+] Domain Cached Credentials 2
[+] DNSSEC(NSEC3)
[+] RAdmin v2.x
```

It's a md5 hash. The output of xxd also have

```
hashlib..md5
```

cracking the hash will give the password as

```
john hash -w=/usr/share/wordlists/rockyou --format=Raw-MD5
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 512/512 AVX512BW 16x3])
Warning: no OpenMP support for this hash type, consider --fork=4
Press 'q' or Ctrl-C to abort, almost any other key for status
!!n0t.@n0th3r.d@mn.p@$$w0rd!! (?)
1g 0:00:00:00 DONE (2022-05-06 20:03) 1.333g/s 19123Kp/s 19123Kc/s 19123KC/s !*baby-gurl*!..!!dogtags$
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed.
```

```
!!n0t.@n0th3r.d@mn.p@$$w0rd!!
```

let’s run the application again.

```
atlansafe2.exe
password : !!n0t.@n0th3r.d@mn.p@$$w0rd!!
[!] decrypting..
STANDCON22{r3v3rs3d_th3_w1n_pyth0n_exe_Q2XO}
```

flag

```
STANDCON22{r3v3rs3d_th3_w1n_pyth0n_exe_Q2XO}
```
