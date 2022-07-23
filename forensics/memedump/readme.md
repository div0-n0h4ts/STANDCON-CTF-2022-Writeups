# MemeDump

Author: Sean (beanbeah)

## Description

I too would like to be a professional meme maker. Sadly, I lack the skill or talent to make such amazing memes. BUT... and hear me out, I got hold of someone's laptop full of dank memes. Well not the laptop, just the memory of the laptop. With this, I should be able to copy all his memes right???? 


## Hints
1. This File is a memory dump, you may need a tool like volatility. 
2. MEMES are made in Microsoft Paint, which is obviously the best editor out there. 


## Note
@nus_it_department has given permission for the use of his memes in this challenge

## Solution
This is intended to be a simple, easy memdump challenge. Tl:dr, extract the memory of microsoft paint, open it in GIMP as raw data, and get the flag. 

1) Get profile of the memdump (this takes a while)
```
vagrant@ctf-box:~/tools/volatility--custom$ python vol.py -f memedump.raw imageinfo
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x86_23418, Win7SP0x86, Win7SP1x86_24000, Win7SP1x86
                     AS Layer1 : IA32PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/ctf-shared/memedump.raw)
                      PAE type : No PAE
                           DTB : 0x185000L
                          KDBG : 0x82958be8L
          Number of Processors : 1
     Image Type (Service Pack) : 0
                KPCR for CPU 0 : 0x82959c00L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2022-05-15 04:18:39 UTC+0000
     Image local date and time : 2022-05-14 21:18:39 -0700
```

The profile is thus `Win7SP0x86`

2) Check list of processes
```
vagrant@ctf-box:~/tools/volatility--custom$ python vol.py -f memedump.raw --profile=Win7SP0x86 pslist
Volatility Foundation Volatility Framework 2.6.1
Offset(V)  Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit
---------- -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0x84e4ac78 System                    4      0     54      367 ------      0 2022-05-15 04:13:25 UTC+0000
0x85cffd40 smss.exe                204      4      2       29 ------      0 2022-05-15 04:13:25 UTC+0000
0x864e1d40 csrss.exe               288    272      8      209      0      0 2022-05-15 04:13:25 UTC+0000
0x86510290 wininit.exe             336    272      3       75      0      0 2022-05-15 04:13:25 UTC+0000
0x86512d40 csrss.exe               344    328      7      202      1      0 2022-05-15 04:13:25 UTC+0000
0x865194e8 winlogon.exe            384    328      3      108      1      0 2022-05-15 04:13:25 UTC+0000
0x8654e290 services.exe            428    336      8      161      0      0 2022-05-15 04:13:25 UTC+0000
0x86556030 lsass.exe               436    336      6      467      0      0 2022-05-15 04:13:25 UTC+0000
0x86558030 lsm.exe                 444    336      9      134      0      0 2022-05-15 04:13:25 UTC+0000
0x865a2990 svchost.exe             556    428     10      333      0      0 2022-05-15 04:13:26 UTC+0000
0x85da7030 svchost.exe             620    428      7      220      0      0 2022-05-15 04:13:26 UTC+0000
0x865cb630 svchost.exe             672    428     16      347      0      0 2022-05-15 04:13:26 UTC+0000
0x874a6588 svchost.exe             752    428     11      282      0      0 2022-05-15 04:13:26 UTC+0000
0x8658d188 svchost.exe             828    428     30      704      0      0 2022-05-15 04:13:26 UTC+0000
0x86626860 svchost.exe             948    428      8      154      0      0 2022-05-15 04:13:26 UTC+0000
0x865fb8e8 svchost.exe            1076    428      5       93      0      0 2022-05-15 04:13:26 UTC+0000
0x86691880 svchost.exe            1120    428      9      293      0      0 2022-05-15 04:13:26 UTC+0000
0x86728030 dwm.exe                1404    752      3       70      1      0 2022-05-15 04:13:27 UTC+0000
0x8672b530 explorer.exe           1416   1380     32      762      1      0 2022-05-15 04:13:27 UTC+0000
0x8674d6e8 taskhost.exe           1480    428      8      145      1      0 2022-05-15 04:13:27 UTC+0000
0x8678b530 Everything.exe         1600   1416      2       59      1      0 2022-05-15 04:13:28 UTC+0000
0x867bd030 dllhost.exe            1936    556     28      537      1      0 2022-05-15 04:14:07 UTC+0000
0x86800a58 WmiPrvSE.exe           1104    556      6      113      0      0 2022-05-15 04:14:27 UTC+0000
0x86787d40 mspaint.exe            1464   1416     12      297      1      0 2022-05-15 04:14:31 UTC+0000
0x84f66d40 svchost.exe             544    428      9      118      0      0 2022-05-15 04:15:26 UTC+0000
0x867ef030 DumpIt.exe             1784   1416      2       39      1      0 2022-05-15 04:18:37 UTC+0000
0x8660b030 conhost.exe            1816    344      2       52      1      0 2022-05-15 04:18:37 UTC+0000
```

That `mspaint` process could be our flag. Other possibilities could be the flag is in the filesystem.

3) Check List of files
We will limit our search to only user Files. (Note, output has been cleaned up of any APPDATA files)
```
vagrant@ctf-box:~/tools/volatility--custom$ python vol.py -f memedump.raw --profile=Win7SP0x86 filescan | grep '.*Users.*'
Volatility Foundation Volatility Framework 2.6.1
0x000000001d309928      8      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Searches\desktop.ini
0x000000003e0086b8      7      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Desktop\Memes\realFlag.png
0x000000003e008770      7      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Desktop\Memes\flag.png
0x000000003e01bc30      1      1 R--rw- \Device\HarddiskVolume2\Users\Administrator\Desktop
0x000000003e01c4a0      8      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Links\Downloads.lnk
0x000000003e5622f0      1      1 R--rw- \Device\HarddiskVolume2\Users\Administrator\Desktop\Memes
0x000000003e562b08      8      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Links\Desktop.lnk
0x000000003e5907c0      5      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Desktop\Memes\genius.png
0x000000003e5f7c90      8      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Videos\desktop.ini
0x000000003e601f80      6      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Desktop\Memes\dank.png
0x000000003e645d40      1      1 RW---- \Device\HarddiskVolume2\Users\Administrator\ntuser.dat.LOG2
0x000000003e647580      1      1 RW---- \Device\HarddiskVolume2\Users\Administrator\NTUSER.DAT
0x000000003e774cc0      8      0 R--rwd \Device\HarddiskVolume2\Users\Public\Videos\desktop.ini
0x000000003e777590      2      1 R--rwd \Device\HarddiskVolume2\Users\Public\Desktop
0x000000003e77aef0      8      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Links\desktop.ini
0x000000003e77fcb8      8      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Favorites\desktop.ini
0x000000003e77fe28      8      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Downloads\desktop.ini
0x000000003e781928      8      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Contacts\desktop.ini
0x000000003e783770      8      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Documents\desktop.ini
0x000000003e784d58      8      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Saved Games\desktop.ini
0x000000003e787600      8      0 R--rwd \Device\HarddiskVolume2\Users\Public\Documents\desktop.ini
0x000000003e78aa98      8      0 R--rwd \Device\HarddiskVolume2\Users\Public\Libraries\desktop.ini
0x000000003e78c038      5      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Desktop\Memes\grassFlag.png
0x000000003e790488      2      1 R--rwd \Device\HarddiskVolume2\Users\Administrator\Desktop
0x000000003e793448      2      1 R--rwd \Device\HarddiskVolume2\Users\Administrator\Desktop
0x000000003e795590      2      1 R--rwd \Device\HarddiskVolume2\Users\Public\Desktop
0x000000003e79b260      4      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Desktop\Memes\mylife.png
0x000000003e7ab110      3      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Desktop\Memes\MONEYYYY.png
0x000000003e7af110      7      0 R--rwd \Device\HarddiskVolume2\Users\Administrator\Desktop\Memes\REDREDFLAG.png
0x000000003ff3d6f0      2      1 R--rwd \Device\HarddiskVolume2\Users\Administrator\Desktop\Memes
```

If you were to extract any of those images, such as `REDREDFLAG.png`, you would realise they are merely memes and not the actual flag. As such, our flag is not in the filesystem but must be within mspaint itself.

4) Extracting mspaint memory
```
vagrant@ctf-box:~/tools/volatility--custom$ python vol.py -f memedump.raw --profile=Win7SP0x86 memdump -p 1464 --dump-dir=.
Volatility Foundation Volatility Framework 2.6.1
************************************************************************
Writing mspaint.exe [  1464] to 1464.dmp
```

5) GIMP
Rename `1464.dmp` to `1464.data`, and open it in GIMP. With some trial and error, the correct offset, width and height can be found. 

![flag](https://i.imgur.com/D0C3pBH.png)

Offset: 192115530
Width: 953
Height: 1024




