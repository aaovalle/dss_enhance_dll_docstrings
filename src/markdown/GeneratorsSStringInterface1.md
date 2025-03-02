# GeneratorsS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr GeneratorsS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string as a result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Generators.Name read

This parameter returns the active generator’s name.

&nbsp;

### Parameter 1: Generators.Name Write

This parameter sets the active generator's name.


***
_Created with the Standard Edition of HelpNDoc: [Modernize your help files with HelpNDoc's WinHelp HLP to CHM conversion tool](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
