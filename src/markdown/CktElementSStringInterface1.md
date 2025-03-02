# CktElementS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr CktElementS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string (pAnsiChar) with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: CktElement.Name

This parameter delivers the full name of the active circuit element.

&nbsp;

### Parameter 1: CktElement.Display - read

This parameter displays the name of the active circuit element (not necessarily unique).

&nbsp;

### Parameter 2: CktElement.Display - write

This parameter allows to modify the name of the active circuit element (not necessarily unique).

&nbsp;

### Parameter 3: CktElement.GUID

This parameter delivers the unique name for the active circuit element.

&nbsp;

### Parameter 4: CktElement.EnergyMeter

This parameter delivers the name of the EnergyMeter linked to the active circuit element.

&nbsp;

### Parameter 5: CktElement.Controller

This parameter delivers the Full name of the i-th controller attached to the active circuit element. The i-th controller index must be specified in the argument arg. Ex: Str = Controller(2). See NumControls to determine valid index range.

&nbsp;

### Parameter 6: CktElement.ActiveVariableName

It can be used to activate a specific state variable by name for the active circuit element. It returns a string “Error” if the variable was not found, otherwise, it will return “OK” signaling that the variable was found and is the active variable.


***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
