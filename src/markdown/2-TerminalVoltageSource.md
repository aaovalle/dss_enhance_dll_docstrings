# 2-Terminal Voltage Source 

&nbsp;

**&#50;-Terminal Voltage Source**

&nbsp;

The Vsource object has been upgraded to a two-terminal voltage source. For connection purposes, it behaves just like the Capacitor, Reactor, and Fault objects. If you define only Bus1, all phases of the Bus2 property are set to the ground node of Bus1. Thus, it will behave just like the one-terminal voltage source.

&nbsp;

All old scripts should work. The Bus2 property was added to the end of the list, so if you've been in the habit of using positional parameters, you should still be OK.

&nbsp;

WARNING: It is now easier to float a circuit and get a numerical error because the Vsource is no longer automatically connected to ground. Be sure you connect any floating sources to something that is referenced to ground.

&nbsp;

This feature is useful for special cases where it is desirable to place a voltage source between two buses or two nodes of the same bus. Some harmonics studies require this. You will no longer have to insert a quasi-ideal transformer to float the source. Simply connect the source between the two buses. For example,

&nbsp;

New Vsource.Hsource Bus1=firstbus Bus2=secondbus basekV=0.48 pu=1.0 R1=1 X1=2 R0=3 X0=4 Spectrum=My

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create Encrypted, Password-Protected PDFs](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
