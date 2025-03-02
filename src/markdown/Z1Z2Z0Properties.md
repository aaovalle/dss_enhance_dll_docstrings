# Z1 Z2 Z0 Properties

&nbsp;

**TechNote Z1 Z2 Z0 Properties**

&nbsp;

*Entering Z1 Z2 Z0 Properties* VSOURCE *and* REACTOR

&nbsp;

As of the 7.6.3.3 version OpenDSS has some new ways to define the symmetrical component impedances of VSOURCE and REACTOR objects.

&nbsp;

You can enter the impedance as a two-element array represent the real and imaginary components. For example:

&nbsp;

Z1=\[1 2\]

&nbsp;

or

&nbsp;

Z1= ”1 2”

&nbsp;

This represents Z1= 1 + j2.

&nbsp;

You can also enter a Z2 value that is different than Z1, which allows you to make equivalents representing rotating machines. The first time you set Z1, the values for Z2 and Z0 are defaulted to the value entered for Z1. Then you can subsequently change Z0 and Z2.

&nbsp;

For VSOURCE devices, you can also specify the sequence impedances in per unit, which is another common way to receive equivalent source data for transmission systems. The property names are: puZ1, puZ0, and puZ2. These must be converted to ohms to be of use to OpenDSS, so the baseMVA property for the VSOURCE object has been added. It defaults to 100 MVA, which is very common for transmission system analysis. So you might not

have to set this property often if you are copying values from transmission power flow programs. Note that some distribution program use a 10 MVA base.

&nbsp;

The base ohms is computed from the basekV and the baseMVA properties.

&nbsp;

As of this writing, the latest build is posted on the Code site under the Distrib folder. You can download the appropriate version from the X86 or X64 folders. See links on: EPRI Link Page [OpenDSS (epri.com)](<https://www.epri.com/pages/sa/opendss?lang=en>)

***
_Created with the Standard Edition of HelpNDoc: [Easy CHM and documentation editor](<https://www.helpndoc.com>)_
