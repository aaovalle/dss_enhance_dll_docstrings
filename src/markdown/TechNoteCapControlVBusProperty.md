# TechNote CapControl VBus Property

&nbsp;

Set this property to the name of a bus you want to monitor for the Voltage Override function of the control. There is no need to set this property if you want the control to monitor the voltage at the terminal where the control is installed. However, there sometimes are occasions where you will want to put the control on a branch terminal other than where the Capacitor is located. Then you can use this property to watch the voltage at the capacitor.

&nbsp;

One example would be where you want to put the capacitor control on the substation for power factor control (Type=PF) of the entire substation. You would typically put all capacitor controls at the substation for this application. Then you can set the VBus property to the name of the bus where the capacitor is actually located.

&nbsp;

You do not need to set this if you are not using voltage override.

&nbsp;

***Wait Until the Bus Exists***

&nbsp;

Define this property AFTER doing an action that causes the OpenDSS to create the buses. Actions that do this are MakeBusList, Solve, and CalcVoltageBases.

&nbsp;

Note: You can define the rest of the properties before the buses exist and then define just the VBus property later, for example, using this syntax:

&nbsp;

CapControl.MyCapControl.Vbus=TheBusIwantToMonitor

***
_Created with the Standard Edition of HelpNDoc: [Save time and frustration with HelpNDoc's WinHelp HLP to CHM conversion feature](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
