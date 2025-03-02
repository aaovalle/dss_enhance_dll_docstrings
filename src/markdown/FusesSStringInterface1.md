# FusesS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr FusesS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Fuses.Name read

This parameter gets the name of the active fuse.

&nbsp;

### Parameter 1: Fuses.Name write

This parameter sets the name of the active fuse.

&nbsp;

### Parameter 2: Fuses.MonitoredObj read

This parameter gets the name of the Monitored Object by the active fuse.

&nbsp;

### Parameter 3: Fuses.MonitoredObj write

This parameter sets the name of the Monitored Object by the active fuse.

&nbsp;

### Parameter 4: Fuses.SwitchedObj read

This parameter gets the full name of the circuit element switch that the fuse controls. Defaults to the MonitoredObj.

&nbsp;

### Parameter 5: Fuses.SwitchedObj write

This parameter sets the full name of the circuit element switch that the fuse controls. Defaults to the MonitoredObj.

&nbsp;

### Parameter 6: Fuses.TCCcurve read

This parameter gets the name of the TCCcurve object that determines fuse blowing.

&nbsp;

### Parameter 7: Fuses.TCCcurve write

This parameter sets the name of the TCCcurve object that determines fuse blowing.


***
_Created with the Standard Edition of HelpNDoc: [Transform Your Help Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com>)_
