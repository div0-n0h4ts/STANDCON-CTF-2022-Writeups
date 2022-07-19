# OMG RNG

Creator - r3yc0n1c

## Description

Gifts for everyone!


## Solution

This challege is based on Multiplicative Lagged Fibonacci Generator
(MLCG) where the next state is generated as -

$$ S_{n} \equiv S_{n-2} * S_{n-1} \pmod{m} $$

where,

m = Prime Modulus,

$S_{n}$ = Current State,

$S_{n-1}$ = Prev State,

$S_{n-2}$ = Prev Prev State

With a little bit of math, we can deduce that -

$$\begin{aligned}
S_{2} &\equiv S_{0} * S_{1} \pmod{m} \\
S_{2} - S_{0} * S_{1} &\equiv 0 \pmod{m} \\
S_{2} - S_{0} * S_{1} &= k_{0} \cdot m \\
S_{3} &\equiv S_{1} * S_{2} \pmod{m} \\
S_{3} - S_{1} * S_{2} &\equiv 0 \pmod{m} \\
S_{3} - S_{1} * S_{2} &= k_{1} \cdot m \\
\end{aligned}$$

$\therefore$ If we take,

$$
GCD(k_{0}, k{1}) = m \\
GCD(S_{3} - S{2} * S{1}, S{2} - S_{1} * S{0}) = m
$$

we can find **m** and then we can run the generator in reverse order to
find the **seeds** ($S_{0}$ and $S_{1}$).

```python
# File: sol.py [line: 9]

curr_state = s[-1]
prev_state = s[-2]

for _ in range(1337 + 4):
    prev_prev_state = curr_state * pow(prev_state,-1,m) % m
    curr_state = prev_state
    prev_state = prev_prev_state

print(curr_state) # s1
print(prev_state) # s0
```

After finding the seeds, the FLAG can be found by **XORing** the
**seeds** and the **secret**.

Files in sol/

## Flag

`STANDCON22{00p5!_W34K_PRNG_5df693c6}`

## References

-   <https://en.wikipedia.org/wiki/Lagged_Fibonacci_generator>
-   <https://en.wikipedia.org/wiki/Secret_sharing_using_the_Chinese_remainder_theorem>
-   <https://proofwiki.org/wiki/GCD_from_Congruence_Modulo_m>
