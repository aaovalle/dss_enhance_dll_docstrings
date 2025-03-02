# RPN Expressions

\
Basically, you enter the same keystrokes as you would with an RPN calculator (such as an HP 48). One difference is that you separate numbers, operators, and functions by a space or comma. The RPN calculator in OpenDSS has a "stack" of 10 registers just like some calculators. In the function descriptions that follow, the first stack register is referred to as "X" and the next higher as "Y" as on the HP calculator. When a new number is entered, the existing registers are rolled up and the new number is inserted into the X register.\
\
These functions operate on the first two registers, X and Y:

&nbsp;

\+&nbsp; &nbsp; Add the last two operands (X and Y registers; result in X; X = X + Y )

\-&nbsp; &nbsp; X = Y - X

\*&nbsp; &nbsp; X = X \* Y

/&nbsp; &nbsp; X = Y / X

\^&nbsp; &nbsp; (exponentiation) X = Y to the X power

&nbsp;

These unitary functions operate on the X register and leave the result in X.&nbsp;

&nbsp;

sqr&nbsp; &nbsp; X=X\*X

sqrt &nbsp; take the square root of X

inv&nbsp; &nbsp; (inverse of X = 1/X)

ln &nbsp; &nbsp; (natural log of X)

exp&nbsp; &nbsp; (e to the X)

log10&nbsp; &nbsp; (Log base 10 of X)

sin &nbsp; &nbsp; &nbsp; &nbsp; for X in degrees, take the sine

cos &nbsp; &nbsp; &nbsp; &nbsp; for X in degrees, take the cosine

tan &nbsp; &nbsp; &nbsp; &nbsp; for X in degrees, take the tangent\
asin &nbsp; &nbsp; &nbsp; take the inverse sine, result in degrees

acos &nbsp; &nbsp; &nbsp; take the inverse cosine, result in degrees

atan &nbsp; &nbsp; &nbsp; take the arc tangent, result in degrees\
atan2&nbsp; take the arc tangent with two arguments, Y=rise and X = run, result in degrees over all four quadrants

&nbsp;

The following functions manipulate the stack of registers

&nbsp;

Rollup &nbsp; &nbsp; shift all registers up

Rolldn &nbsp; &nbsp; shift all registers dn

Swap&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; swap X and Y

&nbsp;

There is one constant preprogrammed: pi

***
_Created with the Standard Edition of HelpNDoc: [Free PDF documentation generator](<https://www.helpndoc.com>)_
