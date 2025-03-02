# RelaysS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr RelaysS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Relays.Name read

This parameter gets the name of the active Relay.

&nbsp;

### Parameter 1: Relays.Name write

This parameter sets the name of the active Relay.

&nbsp;

### Parameter 2: Relays.MonitoredObj read

This parameter gets the full name of the object this relay is monitoring.

&nbsp;

### Parameter 3: Relays.MonitoredObj write

This parameter sets the full name of the object this relay is monitoring.

&nbsp;

### Parameter 4: Relays.SwitchedObj read

This parameter gets the full name of element that will switched when relay trips.

&nbsp;

### Parameter 5: Relays.SwitchedObj write

This parameter sets the full name of element that will switched when relay trips.

&nbsp;

### Parameter 6: Relays.State read

This property gets the present state of relay.

&nbsp;

### Parameter 7: Relays.State write

This property sets the present state of relay. If set to open, open relay's controlled element and lock out the relay. If set to close, close relay's controlled element and resets relay to first operation.

&nbsp;

### Parameter 8: Relays.NormalState read

This property gets the normal state (the state for which the active relay will be forced into at the beginning of the simulation) for the active relay.

&nbsp;

### Parameter 9: Relays.NormalState write

This property sets the normal state (the state for which the active relay will be forced into at the beginning of the simulation) for the active relay.


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Reach: Convert Your Word Document to an ePub or Kindle eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
