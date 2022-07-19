# Incohrent-symbols

**Author:** Mark Bosco

## Category

OSINT

## Question
> An esteemed professor of Atlantean history has disappeared mysteriously, leaving only this note on his desk. Can you discover his login credentials? The flag is STANDCON{professor's_password}. The password is case sensitive.
> Buy hint 1 if you cannot find OOA, buy hint 2 if you cannot unzip the file.


## Solution
1. The text on the picture mentions two people, Oliver Oswald Armadeus, and a Thomas. It also says they had a conversion on the reddit website. 
2. Search for 'Oliver Oswald Armadeus Reddit'. Any number of links could appear, but they should point to the reddit user 'OOArmadeus'.
3. OOArmadeus has asked a question about fonts (https://www.reddit.com/r/Font/comments/ufa53o/hosting_fonts_on_the_internet/)
4. In the question, he includes a link to a ttf font Google Drive download (https://drive.google.com/file/d/12_tLne6kWo7sB-zjLQ-qGQMbh1xTn6Hc/view)
5. Download the ttf file.
6. Decoding the image with the ttf font will give us the string
`thepasswordis
julesverne`

The professor's password is julesverne. Therefore, the flag is STANDCON22{julesverne}.

## Flag
STANDCON22{julesverne}
