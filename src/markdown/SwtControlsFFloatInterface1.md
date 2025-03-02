# SwtControlsF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double SwtControlsF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number (64 bits) with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: SwtControls.Delay read

This parameter gets the time delay \[s\] between arming and opening or closing the switch. Control may reset before actually operating the switch.

&nbsp;

### Parameter 1: SwtControls.Delay write

This parameter sets the time delay \[s\] between arming and opening or closing the switch. Control may reset before actually operating the switch.


***
_Created with the Standard Edition of HelpNDoc: [Easily create Web Help sites](<https://www.helpndoc.com/feature-tour>)_
