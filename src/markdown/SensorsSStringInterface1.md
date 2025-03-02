# SensorsS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr SensorsS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Sensors.Name read

This parameter gets the name of the active sensor object.

&nbsp;

### Parameter 1: Sensors.Name write

This parameter sets the name of the active sensor object.

&nbsp;

### Parameter 2: Sensors.MeteredElement read

This parameter gets the full name of the measured element.

&nbsp;

### Parameter 3: Sensors.MeteredElement write

This parameter sets the full name of the measured element.


***
_Created with the Standard Edition of HelpNDoc: [Create cross-platform Qt Help files](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
