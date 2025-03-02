# TechNote Standard Color Names Added

&nbsp;

Colors for the C1, C2, and C3 properties of the Plot command can now be specified using the standard color names as well as the RGB color number.

&nbsp;

***Standard Color Names***

&nbsp;

Standard color names are:

&nbsp;

• Black

• Maroon

• Green

• Olive

• Navy

• Purple

• Teal

• Gray

• Silver

• Red

• Lime

• Yellow

• Blue

• Fuchsia

• Aqua

• LtGray

• DkGray

• White

&nbsp;

***RGB Color Numbers***

&nbsp;

Any color can be assigned to the C1, C2, and C3 properties simply by assigning the appropriate integer number to the property. The values may be obtained from the Plot Options menu or any other program you might have that can give you the RGB color code. It is common practice to specify the code in hexadecimal format by preceding the number with a "$". For example, a pure red at max intensity could be specified as C1=$000000FF If this format, the digits of a 32bit integer corresponding to the colors are:

&nbsp;

$00bbggrr

&nbsp;

For example, you can get various intensities of green by replacing "gg" with a value between 00 and FF. A full intensity plain green would be

&nbsp;

$0000FF00

&nbsp;

The default for C1 for lines on circuit plots is Blue, or $00FF0000.

***
_Created with the Standard Edition of HelpNDoc: [Don't Let Unauthorized Users View Your PDFs: Learn How to Set Passwords](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
