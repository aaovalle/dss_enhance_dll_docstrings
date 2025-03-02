# LinesS (String) Interface

&nbsp;

This interface can be used to read/modify the properties of the Lines Class where the values are Strings. The structure of the interface is as follows:

&nbsp;

CStr LinesS(int32\_t Parameter, CStr argument)

&nbsp;

This interface returns a string, the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: Lines.Name read

This parameter gets the name of the active Line element.

&nbsp;

### Parameter 1: Lines.Name write

This parameter sets the name of the Line element to set it active.

&nbsp;

### Parameter 2: Lines.Bus1 read

This parameter gets the name of bus for terminal 1.

&nbsp;

### Parameter 3: Lines.Bus1 write

This parameter sets the name of bus for terminal 1.

&nbsp;

### Parameter 4: Lines.Bus2 read

This parameter gets the name of bus for terminal 2.

&nbsp;

### Parameter 5: Lines.Bus2 write

This parameter sets the name of bus for terminal 2.

&nbsp;

### Parameter 6: Lines.LineCode read

This parameter gets the name of LineCode object that defines the impedances.

&nbsp;

### Parameter 7: Lines.LineCode write

This parameter sets the name of LineCode object that defines the impedances.

&nbsp;

### Parameter 8: Lines.Geometry read

This parameter gets the name of the Line geometry code.

&nbsp;

### Parameter 9: Lines.Geometry write

This parameter sets the name of the Line geometry code.

&nbsp;

### Parameter 10: Lines.Spacing read

This parameter gets the name of the Line spacing code.

&nbsp;

### Parameter 11: Lines.Spacing write

This parameter sets the name of the Line spacing code.


***
_Created with the Standard Edition of HelpNDoc: [Upgrade your help files and your workflow with HelpNDoc's WinHelp HLP to CHM conversion](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
