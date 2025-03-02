# CapControlsI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t CapControlsI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: CapControls.First

This parameter sets the first CapControl active. Returns 0 if no more.

&nbsp;

### Parameter 1: CapControls.Next

This parameter sets the next CapControl active. Returns 0 if no more.

&nbsp;

### Parameter 2: CapControls.Mode read

This parameter gets the type of automatic controller (see manual for details).

&nbsp;

### Parameter 3: CapControls.Mode write

This parameter sets the type of automatic controller (see manual for details).

&nbsp;

### Parameter 4: CapControls.MonitoredTerm read

This parameter gets the terminal number on the element that PT and CT are connected to.

&nbsp;

### Parameter 5: CapControls.MonitoredTerm write

This parameter sets the terminal number on the element that PT and CT are connected to.

&nbsp;

### Parameter 6: CapControls.UseVoltOverride read

This parameter gets if Vmin and Vmax are enabled to override the control Mode.

&nbsp;

### Parameter 7: CapControls.UseVoltOverride write

This parameter sets if enables Vmin and Vmax to override the control Mode.

&nbsp;

### Parameter 8: CapControls.Count

This parameter gets the number of CapControls in Active Circuit.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly bring your documentation online with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
