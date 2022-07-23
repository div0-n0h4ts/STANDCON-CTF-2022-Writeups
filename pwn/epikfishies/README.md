# Solution

Simple log4shell exploit

Go through the game

Vulnerable code can be found here:

```java
                if (points == 20) {
                    out.println("You won!");
                    answer = in.readLine();
                    out.println("Your favourite fish: " + answer);
                    c.close();
                }
            }
        } catch (SocketException e) {
            logger.error("Submitted answer: " + answer);
        }
```

When you win, it closes the socket but does not return the function, therefore causes an error.
Do the whole JNDI lookup thingy and point to your own custom LDAP server. Read environment variable `FLAG` for the flag :)

## Flag

`STANDCON22{i_l1ek_fe5h_c0s_th3y_5wim_n_t45+3_n1(3}`
