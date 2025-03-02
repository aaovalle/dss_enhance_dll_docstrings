# MetersS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr MetersS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string according to the number sent in the variable “parameter”. The parameter can be one of the following:

&nbsp;

### Parameter 0: Meters.Name read

This parameter returns the active Energy Meter's name.

&nbsp;

### Parameter 1: Meters.Name Write

This parameter sets the active Energy Meter's name.

&nbsp;

### Parameter 2: Meters.MeteredElement read

This parameter returns the name of the metered element (considering the active Energy Meter).

&nbsp;

### Parameter 3: Meters.MeteredElement Write

This parameter sets the name of the metered element (considering the active Energy Meter).


***
_Created with the Standard Edition of HelpNDoc: [Keep Your PDFs Safe from Unauthorized Access with These Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
