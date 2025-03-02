# RegControlsS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr RegControlsS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: RegControls.Name read

This parameter gets the active RegControl name.

&nbsp;

### Parameter 1: RegControls.Name write

This parameter sets the active RegControl name.

&nbsp;

### Parameter 2: RegControls.MonitoredBus read

This parameter gets the name of the remote regulated bus, in lieu of LDC settings.

&nbsp;

### Parameter 3: RegControls. MonitoredBus write

This parameter sets the name of the remote regulated bus, in lieu of LDC settings.

&nbsp;

### Parameter 4: RegControls.Transformer read

This parameter gets the name of the transformer this regulator controls.

&nbsp;

### Parameter 5: RegControls.Transformer write

This parameter sets the name of the transformer this regulator controls.


***
_Created with the Standard Edition of HelpNDoc: [Easily create EBooks](<https://www.helpndoc.com/feature-tour>)_
