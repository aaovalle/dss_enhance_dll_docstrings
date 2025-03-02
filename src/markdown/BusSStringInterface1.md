# BusS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr BUSS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string according to the number sent in the variable “parameter”. The parameter can be one of the following:

&nbsp;

### Parameter 0: Bus.Name

This parameter returns the name of the active bus.


***
_Created with the Standard Edition of HelpNDoc: [What is a Help Authoring tool?](<https://www.helpauthoringsoftware.com>)_
