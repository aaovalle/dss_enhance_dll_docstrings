# RegControl 

&nbsp;

This control is designed to emulate a standard utility voltage regulator or LTC control. It is attached to a particular winding of a transformer as the winding to monitor. It generally also adjusts the taps in that winding but could also be directed to control the taps in another winding.

&nbsp;

The control has line drop compensator modeling by setting the R, X, CTprim, and ptratio properties. The control can also monitor the voltage at a remote bus to emulate various Smart Grid devices. This is a useful function for performing volt/var optimization.

&nbsp;

To understand how regulator controls work, refer to W. H. Kersting’s book on Distribution System Modeling. A simple example of a regulator on a 12.47 kV system:

&nbsp;

New RegControl.Reg1 Transformer=T1 Winding=2 Vreg=122 band=3 ptratio=60

&nbsp;

With a line-drop compensator, the definition might look like

&nbsp;

New RegControl.Reg1 Transformer=T1 Winding=2 Vreg=122 band=3

\~ ptratio=60 CTprim=300 R=2 X=0

&nbsp;

Controlling a bus at the end of the feeder to 118 V:

&nbsp;

New RegControl.Reg1 Transformer=T1 Winding=2 Vreg=118 band=2 bus=MyEndBus

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Upgrade your help files and your workflow with HelpNDoc's WinHelp HLP to CHM conversion](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
