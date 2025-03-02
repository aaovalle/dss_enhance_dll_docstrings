# CapControlsS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr CapControlsS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: CapControls.Name read

This parameter gets the name of the active CapControl.

&nbsp;

### Parameter 1: CapControls.Name write

This parameter sets a CapControl active by name.

&nbsp;

### Parameter 2: CapControls.Capacitor read

This parameter gets the name of the capacitor that is controlled.

&nbsp;

### Parameter 3: CapControls.Capacitor write

This parameter sets the name of the capacitor that is controlled.

&nbsp;

### Parameter 4: CapControls.MonitoredObj read

This parameter gets the full name of the element that PT and CT are connected to.

&nbsp;

### Parameter 5: CapControls.MonitoredObj write

This parameter sets the full name of the element that PT and CT are connected to.


***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Ease of Use of a Help Authoring Tool](<https://www.helpndoc.com>)_
