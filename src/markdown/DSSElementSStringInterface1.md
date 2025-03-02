# DSSElementS (String) Interface

&nbsp;

This interface can be used to read/modify the properties of the DSSElement Class where the values are Strings. The structure of the interface is as follows:

&nbsp;

CStr DSSElementS(int32\_t Parameter, CStr argument) ;

&nbsp;

This interface returns a string, the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: DSSElement.Name

This parameter gets the full name of the active DSS object (general element or circuit element).


***
_Created with the Standard Edition of HelpNDoc: [Streamline your documentation process with HelpNDoc's WinHelp HLP to CHM conversion feature](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
