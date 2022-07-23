We were given a binary.txt that contains nothing but 0's and 1's. From
the description, it says a message encrypted by XOR is placed somewhere
within this file

![A picture containing background pattern Description automatically
generated](images/media/image1.png)

To approach this, I decided to write a script using python using the
logic below. Knowing that ASCII characters are represented by 8 bits, I
can decrypt every 8-bit using the key and convert it from binary to
ASCII.

0100101011001111101100101

However, knowing that the message is injected at a random position, I
can't assume that the message will be located at the position of
multiples of 8. Instead, I would need to go through every position and
obtain the 8-bit from that position for the decryption

  ***Incorrect Decryption***   ***Correct Decryption***
  ---------------------------- ---------------------------
  0100101011001111101100101    0100101011001111101100101
  0100101011001111101100101    0100101011001111101100101
  0100101011001111101100101    0100101011001111101100101

So when a byte is decrypted and turns out to be a valid printable ASCII
character (a,b,c,d,e....), I can assume that the next valid character
will be the next 8-bit thus, obtaining a possible message.

[Example:]{.ul}

The script would print the message "HE" from the example bellow

1010010000100010111010100 **Gives Rubbish**

**\| Next step (Since Invalid char, decrypt next position byte)**

1010010000100010111010100 **Gives H**

**\| Next step (Since valid char, decrypt next multiple of 8 position
byte)**

1010010000100010111010100 **Gives E**

**\| Next Step (Since valid char, decrypt next multiple of 8 position
byte)**

1010010000100010111010100 **Gives Rubbish**

**\| Next Step (Since Invalid char, decrypt next position byte from
where it discontinued)**

1010010000100010111010100 **Gives Rubbish**

Using the logic above, I created a script. I made it to dump the
possible messages on a file and it turns out there are lots of red
herrings. Over 1 million+ of printable ASCII characters.

![A picture containing text Description automatically
generated](images/media/image2.png)

Using a very powerful shortcut and useful shortcut ctrl-f, I tried to
see if the message contained the flag. However, placing the string
STANDCON22 in the find command gave me nothing.

![Graphical user interface, text Description automatically
generated](images/media/image3.png)

During the process of finding, I found something. There was a match for
the string "STAND"

![Graphical user interface Description automatically
generated](images/media/image4.png)

Assuming the flag got split and then injected into this file, I assumed
the string "CON" should also exist, which did.

![Background pattern Description automatically
generated](images/media/image5.png)

Next, the very important part of the flag should be in the following
syntax {.......}. There is also a possibility that this part got split
thus it would be effective to use regex.

Also, I noticed that the position of "STAND" was at 127820 and "CON22"
was at 299793. Even though it was mentioned the message got injected
randomly, it was not truly random. They might have been placed in order
from left to right, but this is a huge assumption I'm making.

So, I updated my script to retrieve strings that started with "{" from
position 299793 onwards. Also, I filtered out any strings that were less
than 5 characters to reduce noise. This was what it gave me.

![A picture containing text Description automatically
generated](images/media/image6.png)

One of those strings caught my attention which was "{x0r_15\_" which
looks like it is part of the flag. Continuing, I found its position
(705963). Assuming I am finding the last part of the flag already, I
updated my script to retrieve strings that ended with "}" from position
705963 onwards.

This was my result. I believed the last string was the final piece of
the puzzle. Putting all the pieces together, I got:
STANDCON22{x0r_15_51mpl3}

![Text Description automatically
generated](images/media/image7.png)
