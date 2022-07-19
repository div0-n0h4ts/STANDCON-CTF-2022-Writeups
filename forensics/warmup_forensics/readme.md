# Warmup Forensics

Author: Sean (beanbeah)

## Description

Forensics Warmup!!! This challenge should take you less than 133.7 seconds to solve!

## Hints
1. This File is a PNG File
2. Have you heard of a hex editor?


## Solution
1) Notice the PNG Signature and size is wrong (set to STANDCON22)

Fixed Signature and Size
![pngsig](https://i.imgur.com/9oUDKbO.png)

2) Notice the height and width values are wrong (set to 0)

![png](https://i.imgur.com/jp8E9nh_d.webp?maxwidth=1520&fidelity=grand)
With the file header fixed, we can also spot that the width and height are both set to 0. We can simply change the width and height values to repair the PNG. In this case, the correct width and height values are `1920` and `1080` respectively. (note, 1920*1080 is also a common screen size used). 

Repaired Image:

![image](org.png)




