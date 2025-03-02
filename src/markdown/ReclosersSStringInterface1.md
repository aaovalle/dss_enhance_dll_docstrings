# ReclosersS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr ReclosersS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Reclosers.Name read

This parameter gets the name of the active Recloser Object.

&nbsp;

### Parameter 1: Reclosers.Name write

This parameter sets the name of the active Recloser Object.

&nbsp;

### Parameter 2: Reclosers.MonitoredObj read

This parameter gets the full name of object this Recloser is monitoring.

&nbsp;

### Parameter 3: Reclosers.MonitoredObj write

This parameter sets the full name of object this Recloser is monitoring.

&nbsp;

### Parameter 4: Reclosers.SwitchedObj read

This parameter gets the full name of the circuit element that is being switched by this Recloser.

&nbsp;

### Parameter 5: Reclosers.SwitchedObj write

This parameter sets the full name of the circuit element that is being switched by this Recloser.

&nbsp;

### Parameter 6: Reclosers.State read

This property gets the present state of recloser. If set to open, open recloser's controlled element and lock out the recloser. If set to close, close recloser's controlled and resets recloser to first operation.

&nbsp;

### Parameter 7: Reclosers.State write

This property sets the present state of recloser. If set to open, open recloser's controlled element and lock out the recloser. If set to close, close recloser's controlled and resets recloser to first operation.

&nbsp;

### Parameter 8: Reclosers.NormalState read

This property gets the normal state (the state for which the active recloser will be forced into at the beginning of the simulation) for the active recloser.

&nbsp;

### Parameter 9: Reclosers.NormalState write

This property sets the normal state (the state for which the active recloser will be forced into at the beginning of the simulation) for the active recloser.


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Convert Your Word Doc to an eBook: A Step-by-Step Guide](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
