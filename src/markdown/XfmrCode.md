# XfmrCode

&nbsp;

Like LineCode for Line objects, you can define transformer objects and use them simply by referring to them in the Transformer object definition using the XfmrCode property. The XfmrCode properties generally have the same name and definition as the Transformer object. Refer to the Transformer object definition.

&nbsp;

An example use of an XfmrCode to define a bank of 1-phase transformers to make up a 3-winding Y-D-Y connection:

&nbsp;

// The Transformer

// Model as 3 1-phase transformers so we can see the delta currents

New XfmrCode.YDY1Phase phases=1 windings=3

\~ conns=\[wye wye delta \]

\~ kVs=\[39.83, 7.62, 2.4\]

\~ kVAs=\[5000 3333 1666\] \! 15 MVA 3-phase

\~ XHL=7.5 XHT=36 XLT=28

\~ %Rs = \[0.11 0.11 0.275\]

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

To define the Transformers, only need to specify buses and any other

properties that are different.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

// Connect up the three 1-ph transformer in YYD

New Transformer.YDYA XfmrCode=YDY1Phase ppm=0 \!\<--------neglect ppm

\~ Buses=\[B2.1.0 B3.1.0 B5.1.2\]

New Transformer.YDYB XfmrCode=YDY1Phase ppm=0

\~ Buses=\[B2.2.0 B3.2.0 B5.2.3\]

New Transformer.YDYC XfmrCode=YDY1Phase ppm=0

\~ Buses=\[B2.3.0 B3.3.0 B5.3.1\]

&nbsp;

&nbsp;

A transformer “bank” has also been added, as a property on existing transformer objects. At present, this is used only for Common Information Model (CIM) export, but the concept may be extended as needed for MultiSpeak interfaces, and for output reports. Switches, capacitors, and even loads are often grouped into “banks” for identification.

&nbsp;

**XfmrCode and Bank**

&nbsp;

The new XfmrCode object has every property of the Transformer object, except for bank, bus, buses, and xfmrcode. You can specify transformer parameters on the XfmrCode object, and then re‐use them through the new xfmrcode property on the Transformer. (It was previously possible to mimic a

transformer library using the like property, but this had the disadvantage of creating “phantom buses” for the library transformer objects.)

&nbsp;

The following example from the IEEE 13‐bus test case illustrates both xfmrcode and bank. At present, the only effect of bank is that, when executing the “export cdpsm” command, the three regulator legs will be grouped into one bank as required by the CIM.

&nbsp;

New XfmrCode.RegLeg phases=1 xhl=0.01 kvas=\[1666 1666\] kvs=\[2.4 2.4\] %LoadLoss=0.01

&nbsp;

New Transformer.Reg1 XfmrCode=RegLeg Bank=Reg Buses=\[650.1 RG60.1\]

New Transformer.Reg2 XfmrCode=RegLeg Bank=Reg Buses=\[650.2 RG60.2\]

New Transformer.Reg3 XfmrCode=RegLeg Bank=Reg Buses=\[650.3 RG60.3\]


***
_Created with the Standard Edition of HelpNDoc: [Make your documentation accessible on any device with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
