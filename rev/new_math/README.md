## Solution to New Math

Running "file" on NewMath reveals that it is a TI-84 graphing calculator binary (.8xp file). To run the binary, you can either transfer it to your own graphing calculator, or use the emulator provided by Texas Instruments. 

Adding the .8xp file extension and running the binary shows that it is some sort of Math quiz, which prompts the user for the answers to two questions. If both questions were correctly answered, the flag would be plotted as a graph. 

Using a decompiler for .8xp files such as https://github.com/Lekensteyn/parse8xp, the logic of the binary can be seen (raw decompilation):

```
NEWMATH
not protected
Created by TI Connect CE 5.6.3.2278
ClrHome
Disp "C&stata&statn yo&u &statdo &statn&state&w m&stata&statth?"
Disp ""
Disp "P&statr&state&stats&stats ENTER &statto &statco&statn&statti&statn&u&state"
Pause 

ClrHome
Input "E&statn&statt&state&statr &statth&state m&statagi&statc &statn&um&statb&state&statr: ",A
&@�FnOff A)->Str1
"1"+Str1->Str2
Str1+"1"->Str3
expr(Str2)->B
expr(Str3)->C

If 3B=C and length(Str1)=5
Then
Disp "Co&statr&statr&state&statc&statt!" 
ClrHome
Disp "E&statn&statt&state&statr &statth&state &stats&state&statco&statn&statd"
Input "m&statagi&statc &statn&um&statb&state&statr: ",D
If abs(fMax(&-2X^2+25X+4,X,0,10)-D)<0.01
Then
Disp "Yo&u go&statt f&ull m&stata&statrk&stats!"
Disp "YOU WIN"
ClrDraw
ZStandard
&-2->&@c&rad
34->&@c&deg
&-4->&@c&^-1
4->&@c&^2

Line(8,0,10,0)
Line(100/D,1,100/D,2)
Line(100/D,1,(D+50)/3.125,1)
Line((A-27232)^(1/3),0,(D*6)-10.5,1000*0*20)
Line((A-15209)/1024,1,52-23,100-99)
Line((A-D-42822.75),0,A-D*44-42554,2)
Line(30,0,30,2)
Line(2*D+8.5,0,2*D+8.5+2,0)
Line((A-41477)/60,0,&squareroot(576),2)
Line(23.5,1,24.5,1)
Line(150/D,60-58,&squareroot(A-42232),0)
Line(62.5/D,2,12,A/21428.5)
Line(0,0,0,12.5/D)
Line(B/(71424.5+4),0,C*0,&squareroot(39.0625)/3.125)
Line(2,0,(C-6585)/210993,(B-6353)/68252)
Circle(D/1.5625,3-2,D-5.25)
Line(D-0.25,2,D+1.75,10/5)
Line(43.75/D,0,C-428564,4-2)
Line(187.5/D,0,(A-28297)/455,0)
Line(&squareroot(D*144),98-96,(A-24809)/564,100-98)
Line((A-5003)/2103,9-8,(B-132615)/569,0)
Line((A-32139)/653,0,18,0)
Line((A-19031)/1254,48-46,D+14.75,2)
Line(&squareroot(A-42457),0,&squareroot(A-42457),2)
Line(A-42846,0,A-42846,7-5)
Line(10,1,A-42846,0)
Line(C/32967,0,81.25/D,4-2)
Line(B/10989,0,B-142842,0)
Line(15,0,15,2)
Line(16,2,18,2)

Else
Disp "Yo&u &statt&statri&state&statd, &statb&u&statt yo&u &stats&stattill"
Disp "&statc&stata&statn'&statt &statdo M&stata&statth :("
Disp "YOU LOSE"
End
Else
Disp "Yo&u f&statail&state&statd yo&u&statr m&stata&statth &statt&state&stats&statt :("
Disp "YOU LOSE"
End 
```
#### Question 1

The first question seems to involve the logic as shown:

```
"1"+Str1->Str2
Str1+"1"->Str3
expr(Str2)->B
expr(Str3)->C

If 3B=C and length(Str1)=5
```
The length of the input has to be greater than 5. If a "1" is added to the front of the 5-digit number, the resultant number would be 3 times smaller than if the "1" was added to the end of the number. This is a math puzzle from https://www.mathsisfun.com/puzzles/5-digit-number.html and the answer is 42857..

#### Question 2

The second question seems to involve the logic as shown: 

```
If abs(fMax(&-2X^2+25X+4,X,0,10)-D)<0.01
```
This is a classic graphing calculator "find the x-value of the maximum point of a quadratic curve" problem. Do this on a graphing calculator/desmos and you will realize that the answer is 6.25. 

Once both questions have been successfully solved, the flag will be graphed out on the screen :D

Flag: STANDCON22{NOT_JUST_A_+C}
