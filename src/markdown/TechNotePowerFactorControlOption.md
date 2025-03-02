# TechNote Power Factor Control Option added to CapControl

&nbsp;

***Power Factor Control Option added to CapControl***

&nbsp;

You can define a CapControl as PF control. This is designed for representing control systems that attempt to maintain a certain power factor at the substation bus or some other bus by controlling several capacitor banks.

&nbsp;

You can define one or more CapControl objects to monitor the same terminal value. Each one controls a single capacitor bank. You control the sequencing by setting the Delay and DelayOFF properties of the CapControl.

&nbsp;

The ONsetting and OFFsetting properties default to 0.95 and 0.95, respectively, when you set the control type to PF. Negative values are used to represent leading power factor (negative vars looking into the terminal the control is monitoring).

&nbsp;

***Example:***

&nbsp;

The following script defines two capacitors controlled from the same line terminal voltage and current, turning the capacitors ON when the PF drops more lagging than 0.98 lead. The capacitors are turned off when the PF is more leading than 0.94.

&nbsp;

New Capacitor.C1 Bus1=MVBus2 kV=12.47 kvar=300

New CapControl.C1 element=Line.Line1 Terminal=1 Capacitor=C1 Type=PF ONsetting=.98 OFFsetting=.94 Delay=...

New Capacitor.C2 Bus1=MVBus2 kV=12.47 kvar=300

New CapControl.C2 element=Line.Line1 Terminal=1 Capacitor=C2 Type=PF ONsetting=.98 OFFsetting=.94 Delay=...

&nbsp;

**Hint:**

Be sure to inspect the Event log (show event) after running a simulation. This has been made more verbose and readable to help you debug control actions. You can see when Capacitors are armed to operate and when they actually do.

***
_Created with the Standard Edition of HelpNDoc: [iPhone web sites made easy](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
