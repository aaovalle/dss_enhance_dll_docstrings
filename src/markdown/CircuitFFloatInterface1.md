# CircuitF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double CircuitF(int32\_t Parameter, double Argument1, double Argument2);

&nbsp;

This interface returns a floating point number (IEEE754 64 bits) according to the number sent in the variable “parameter”. The parameter can be one of the following:

&nbsp;

### Parameter 0: Circuit.Capacity

This parameter returns the total capacity of the active circuit. Or this parameter it is necessary to specify the start and increment of the capacity in the arguments argument1 and argument2 respectively. 


***
_Created with the Standard Edition of HelpNDoc: [Save time and frustration with HelpNDoc's WinHelp HLP to CHM conversion feature](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
