# STANDCON CTF Write Up

![Untitled](images/Untitled.png)

Initial ARP messages tell you that there is clearly no 192.168.10.99 available. This should give some signal that the connection is not happening.

![Untitled](images/Untitled%201.png)

Suddenly, there’s another ARP message appearing which redirects the target to it (now a new player with 192.168.10.145)

![Untitled](images/Untitled%202.png)

The moment there’s some connection, it’s trying to reach to n0h4ts

![Untitled](images/Untitled%203.png)

ICMP showing that the man-in-the-middle is allowing connection to internet.

![Untitled](images/Untitled%204.png)

Notice there’s an HTTP clear text get from the IP address.

![Untitled](images/Untitled%205.png)

Bleah I didn’t close the bloody HTML and body. But the encoded message is there.

![Untitled](images/Untitled%206.png)

Flag is in the decoding.
