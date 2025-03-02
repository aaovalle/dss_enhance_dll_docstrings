# Multi-Line Commands

&nbsp;

If a command needs to span multiple lines, the ~ symbol (which is an alias for the More command) should be used, such as in the example below:

&nbsp;

New Line.L1 Bus1=1, Bus2=2, Length=1

\~ units=mi, geometry=3PH\_3/0\_Horiz

&nbsp;

Note that the above code is actually technically two separate commands. As such, any nondefault parameters that must be defined at instantiation of an Element Class must be defined in the first line. Thus, the following would generate an error:

&nbsp;

// This will error because Bus1 and Bus2 are not set in the first line

New Line.L1 Length=1, units=mi

\~ Bus1=1, Bus2=2, geometry=3PH\_3/0\_Horiz

***
_Created with the Standard Edition of HelpNDoc: [Protect Your Confidential PDFs with These Simple Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
