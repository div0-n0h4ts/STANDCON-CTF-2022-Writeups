
Creator: Ravindu (@rvizx9)

Category: Misc

# Description

We found a safe from Atlantis. Sang Nila Utama’s crown must be inside it. Can you crack the safe?

# Hints

1. * at once
2. you rock you rock

You can use the “GraphicsMagic” and read every frame of the GIF separately which will take more time and put together.

```
gm convert image.gif -coalesce +adjoin image_frame%3d.png
```

OR

You can use “zbarimage” at once.

```
zbarimage image.GIF
```

Then the ASCII QR Code will be there. 

```
	##############      ##  ##    ##    ##############
        ##          ##  ##  ##    ##  ####  ##          ##
        ##  ######  ##          ##    ##    ##  ######  ##
        ##  ######  ##  ######  ##    ##    ##  ######  ##
        ##  ######  ##    ##        ####    ##  ######  ##
        ##          ##  ####  ######        ##          ##
        ##############  ##  ##  ##  ##  ##  ##############
                          ######  ##
        ##########  ########  ##      ######  ##  ##  ##
        ######  ####    ##  ##  ######    ##  ####  ####
        ######    ####      ##      ######      ####    ##
          ##  ##  ##    ##      ##  ##  ##  ####  ##    ##
        ######      ##    ####  ####  ##  ####        ##
        ##    ##  ##  ##  ##      ##    ######
        ##          ######    ####    ##  ########  ##  ##
        ##  ####  ##      ##  ##      ##    ##  ##    ####
        ##          ##  ##    ##  ##################
                        ####    ##    ####      ####  ##
        ##############  ##              ##  ##  ####
        ##          ##          ##  ######      ######  ##
        ##  ######  ##  ######  ##      ##############  ##
        ##  ######  ##  ##          ######  ##  ##    ####
        ##  ######  ##  ##  ######      ##      ##  ##  ##
        ##          ##  ####  ##        ##########
        ##############  ####  ####        ######        ##
```

Which gives you the password of the zip file.

```
KEY 230K-YUI9-3XDE-R97Z-5X3D-L4E8
```

The kdbx file is a KeePass2 file. Which can be cracked using keepass2john + hashcat or john.

# Cracking the kdbx file

```python
keepass2john Database.kdbx > hash.txt

```

before cracking the hash you've to use the hint otherwise it'll take very long time to crack the hash.
you rock means the reverse of rockyou so you've to reverse the wordlist

fastest way to do this is using tac, and to remove space characters infront of each word we can use sed.

```bash
tac /usr/share/wordlists/rockyou.txt | sed 's/^ *//g' >  yourock.txt
```

then you can crack the hash using the new wordlist

```
hashcat -m 13400 -a 0 -w 1 hash /usr/share/wordlists/yourock.txt
```

or

```
john hash --wordlist=/usr/share/wordlists/yourock.txt
```

Before cracking the hash make sure to remove the DBName part from the hash.

password is 

```
b503290174
```

with that password, we can extract “AtlanSafe.exe” file from the compressed 7z file.
If we use dnSpy or ILspy  we can easily explore the functions and everything of the application.

pin

```csharp
// Token: 0x0600001A RID: 26 RVA: 0x00002EFC File Offset: 0x000010FC
		private void btnExec_Click(object sender, EventArgs e)
		{
			this.richtbx.Text = "Initializing...\nChecking PIN\n";
			bool flag = this.txtpin.Text != "7689";
```

```csharp
pin=7689
```

Then if we check button click events on UserLogin

```csharp
// ATLAN_Safe.LoginUser
// Token: 0x06000005 RID: 5 RVA: 0x00002074 File Offset: 0x00000274
private void button1_Click(object sender, EventArgs e)
{
	bool flag = this.txtBox1.Text != "rvizx9";
	if (flag)
```

```csharp
username=rvizx9
```

After that “UserPassword” function checks userinput against the md5 hash of the password

```csharp
public void button1_Click_1(object sender, EventArgs e)
{
	bool flag = LoginPass.ComputeMd5Hash(this.txtPass.Text).ToLower() == "532109e0eba9ef0279b6cccfca6c6c03";
	if (flag)
	{
```

```
532109e0eba9ef0279b6cccfca6c6c03
```

this can be cracked with the new yourock.txt in a few seconds, and password is;

```
!#udamnHACKER#!
```

that’s it.

Now run the app and get the flag.

# Flag

```
STANDCON22{cr4ck3d_th3_sup3r_s3cur3d_4tl4n_s4f3_0x34PEIOVKO23XZRVPJQLER}
```
