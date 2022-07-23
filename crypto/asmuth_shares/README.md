# Asmuth Shares

Creator - r3yc0n1c

## Description

Asmuth wants to share something with you!


## Solution

This challenge is based on the Asmuth-Bloom Secret Sharing Scheme where
the secret shares are created as follows -

$$\begin{aligned}
s_{0} &= FLAG + A \cdot m_{0} \pmod{m_{1}} \\
s_{1} &= FLAG + A \cdot m_{0} \pmod{m_{2}} \\
s_{2} &= FLAG + A \cdot m_{0} \pmod{m_{3}} \\
&\vdots \\
s_{i} &= FLAG + A \cdot m_{0} \pmod{m_{i+1}} \\
\end{aligned}$$

where $s_{i}$ is the $i^{th}$ share, A is a random number, $m_{i}$ is
the $i^{th}$ prime.

So, we can solve this system using CRT with some shares and get a
solution such that,

$$res = FLAG + A \cdot m_{0}$$

If we take $\pmod{m_{0}}$ of res then,

$$\begin{aligned}
res &= FLAG + 0 \pmod{m_{0}} \\
res &= FLAG \pmod{m_{0}} \\
\because n \cdot A &= 0 \pmod{A}
\end{aligned}$$

Files in sol/

## Flag

`STANDCON22{CRT_F0r_7h3_W1n_38a9c56b}`

## References

-   <https://en.wikipedia.org/wiki/Chinese_remainder_theorem>
-   <https://en.wikipedia.org/wiki/Secret_sharing_using_the_Chinese_remainder_theorem>
-   <https://www.researchgate.net/publication/309027457_A_CRT-based_verifiable_secret_sharing_scheme_secure_against_unbounded_adversaries>
