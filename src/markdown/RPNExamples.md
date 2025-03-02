# RPN Examples

&nbsp;

For example, the following DSS code will calculate X1 for a 1-mH inductance using inline RPN:

&nbsp;

// convert 1 mH to ohms at 60 Hz, note the last \* operator

line.L1.X1 = (2 pi \* 60 \* .001 \*)

&nbsp;

The expression in parentheses is evaluated left-to-right. '2' is entered followed by 'pi'. Then the two are multiplied together yielding ![Image](<lib/eq7.png>). The result is then multiplied by 60 to yield ![Image](<lib/eq8.png>) . Finally, the result is multiplied by 1 mH to yield the reactance at 60 Hz. To specify the values of an array using in-line math, simply nest the quotes or parentheses:

&nbsp;

// Convert 300 kvar to 14.4 kV, 2 steps

Capacitor.C1.kvar = \[(14.4 13.8 / sqr 300 \*), (14.4 13.8 / sqr 300 \*)\]

&nbsp;

The Edit \| RPN Evaluator menu command brings up a modal form in which you can enter an RPN expression and compute the result. Clicking the OK button on this form automatically copies the result to the clipboard. The purpose of this feature is to enable you to interpret RPN strings you find in the DSS script or to simplify the above script by computing the result and replacing the RPN string with the final value if you choose:

&nbsp;

Capacitor.C1.kvar = \[ 326.65, 326.65\] \! 300 kvar converted to 14.4 kV, 2 steps

&nbsp;

This next example shows how to use RPN expressions inside an array. Two different delimiter types are necessary to differentiate the array from the expressions.

&nbsp;

// set the winding kvs to (14.4 20)

New Transformer.t kvs=("24.9 3 sqrt /" "10 2 \*")

***
_Created with the Standard Edition of HelpNDoc: [Make Your PDFs More Secure with Encryption and Password Protection](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
