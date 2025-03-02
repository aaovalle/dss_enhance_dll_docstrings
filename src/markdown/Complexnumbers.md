# Complex numbers

\
Since version 10.2 OpenDSS supports complex number notation. This notation is used by the properties InjCurrent, ITerminal, and YPrim used for getting and setting the injection currents, currents at the terminal and Y primitive matrix for PCE (see [Options](<Options.md>)).

&nbsp;

For entering a complex number to OpenDSS users must follow these guidelines:

&nbsp;

1. &nbsp;
   1. The suffix for the imaginary part of the number can be the character "i" or "j". No other character will have the same effect and may lead to the identification of the imaginary part as zero (0).
   1. No spaces (" ") can be part of the complex number declaration.

&nbsp;

Following these directives will prevent the collapse of the simulation. Below are some examples demonstrating how to use complex numbers in OpenDSS.

&nbsp;

&nbsp;&nbsp; Select Load.myload

&nbsp;

&nbsp;&nbsp; Set Yprim=\[1+1j \| 1+1j 2+2j \| 1+1j 2+2j 3+3j\]&nbsp; \!declares a 3x3 y primitive matrix for the active load

&nbsp;

&nbsp;&nbsp; Set InjCurrent=\[1.2-0.5i 3.432+2,45i -1.23-0.98i\]&nbsp; \!Sets the inj currents for the active load

***
_Created with the Standard Edition of HelpNDoc: [Bring your WinHelp HLP help files into the present with HelpNDoc's easy CHM conversion](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
