# CapControl

&nbsp;

The capacitor control monitors the voltage and current at a terminal of a PDelement or a PCelement and sends switching messages to a Capacitor object. The CapControl contains essential features of many typical utility capacitor controls.

&nbsp;

Example:

&nbsp;

New CapControl.C1ctrl element=Line.L1 Capacitor=C1

\~ Type=Current ON=400 OFF=300 Delay=30

&nbsp;

This control monitors the current in Line.L1 and switches Capacitor.C1 based on current magnitude. This is one of the simpler controls to implement. The capacitor will switch ON when the current in the monitored phase (defaults to 1) after a delay of 30 s. If the current drops below 400 A before 30 s has elapsed, the control resets (ignores the message from the control queue).

&nbsp;

After energization, the capacitor switches off when the current drops below 300 with the default DelayOFF.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Productivity with HelpNDoc's CHM Help File Creation Features](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
