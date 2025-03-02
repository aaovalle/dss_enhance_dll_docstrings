# RPN Calculator

&nbsp;

***RPN Calculations in DSS***

&nbsp;

The DSS scripting language uses a form of RPN to accommodate inline math. The parser will evaluate RPN expresssion automatically simply by enclosing the expression in any of the quoted formats (quotation marks or any of the matched parens, brackets, etc.). For example, considering the following DSS code for specifying X1 from the inductance of 1 mH using inline RPN:

&nbsp;

line.L1.X1 = (2 pi \* 60 \* .001 \*) \! 1 mH to ohms at 60 Hz \! don't forget the last operator\!

&nbsp;

The expression the parens is evaluated lefttoright. '2' is entered followed by 'pi'. then the two are multiplied together yielding 2π. The result is then multipled by 60 to yield ω (2πf). Finally, the result is multiplied by 1 mH to yield the reactance at 60 Hz. To specify the values of an array using inline

math, simply nest the quotes or parantheses:

&nbsp;

Capacitor.C1.kvar = \[(14.4 13.8 / sqr 300 \*), (14.4 13.8 / sqr 300 \*)\] \! Convert 300 kvar to 14.4 kV, 2&nbsp;

&nbsp;

***RPN Evaluator Form***

&nbsp;

There is now an RPN evaluator that appears under the Edit \| RPN Evaluator menu item. This brings up a modal form in which you can enter an RPN expression and compute the result. Clicking the OK button on this form automatically copies the result to the clipboard. The purpose of this feature is to enable you to interpret RPN strings you find in the DSS script or to simplify the above script by computing the result and replacing the RPN string with

the final value if you choose:

&nbsp;

Capacitor.C1.kvar = \[ 326.65, 326.65\] \! 300 kvar converted to 14.4 kV, 2 steps

&nbsp;

**RPN Expressions**

&nbsp;

Basically, you enter the same keystrokes as you would using a RPN calculator (such as an HP 48). One difference is that you separate numbers, operators, and functions by a space or comma. The RPN calculator has a "stack" of registers just like an actual calculator, except that it is basically unlimited. In the text below, the main entry register is referred to as "X" and the next higher as "Y" like on the traditional calculator. When a new number is entered, the existing registers are rolled up and the new number is inserted in the X register.

&nbsp;

***Operators***

&nbsp;

\+ Add the last two operands (X and Y registers; result in X; X = X + Y )

\- X = Y - X

\* X = X \* Y

/ X = Y / X

\^ (exponentiation) X = Y to the X power

&nbsp;

**Functions**

&nbsp;

The following functions operate on the X register and leave the result in X.

&nbsp;

sqrt (take square root of X) sqr (X=X\*X)

Trig functions: (specify X in DEGREES) sin, cos, tan, asin, acos, atan atan2 (Y=rise, X=run)

inv (inverse of X = 1/X)

ln (natural log of X)

exp (e to the X)

log10 (Log base 10 of X)

&nbsp;

**Register Functions**

&nbsp;

The following functions operate on the registers

&nbsp;

rollup shift all registers up

rolldn shift all registers dn

swap swap X and Y

&nbsp;

**Constant**

&nbsp;

There is currently one constant pre-programmed: pi

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Experience the power of a responsive website for your documentation](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
