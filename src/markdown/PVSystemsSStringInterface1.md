# PVSystemsS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr PVSystemsS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: PVSystems.Name read

This parameter gets the name of the active PVSystem.

&nbsp;

### Parameter 1: PVSystems.Name write

This parameter sets the name of the active PVSystem.

&nbsp;

### Parameter 2: PVSystems.Sensor

This parameter returns the name of the sensor monitoring the active PV System.


***
_Created with the Standard Edition of HelpNDoc: [Create cross-platform Qt Help files](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
