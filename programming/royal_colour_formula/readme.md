# Royal-Colour-Formula

**Author:** Mark Bosco

## Category

Programming

## Question
> The study of Atlantean culture is endlessly fascinating. Professor Armadeus has written a short piece on the Royal Colour Formula.
> The flag you seek will appear if you manage to compute the previous Royal Colours.


## Solution
Observe the RGB values of each colour, and compare them with the corresponding colour of the previous ruler. 
To produce the next colour, each the red, green, or blue value of the colour is the sum of the other two values of the previous colour (subtract 255 if it is greater).
(see Royal_Colour_generate.html for a script)

Therefore to find the previous colour, there are three steps:
1. To find the red value, add the red value and blue value of the previous colour.
2. Subtract the blue value of the previous colour.
3. Divide by 2. If result is more than 255, subtract 255.

Repeat this two more times to find the green, and blue values

Example using algebra:
current colour: rgb(a+b,b+c,c+a)
previous colour: rgb(a,b,c)

a = ((a+b)+(c+a)-(b+c)) / 2

Starting with the most recent colour combination (#8b788a,#71707b,#5d415e,#5d2e14,#0c141e,#c2b9d2,#9589a0,#e1d5c7,#003c04), run the reverse formula several times. Each time, try decoding the rgb values to ascii.
After 20 iterations, the flag should appear.

## Flag
STANDCON22{LUCK_OF_THE_SEA}