# IsourcesI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t IsourcesI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Isources.Count

This parameter returns the number of Isource objects currently defined in the active circuit.

&nbsp;

### Parameter 1: Isources.First

This parameter sets the first ISource to be active; returns 0 if none.

&nbsp;

### Parameter 2: Isources.Next

This parameter sets the next ISource to be active; returns 0 if none.


***
_Created with the Standard Edition of HelpNDoc: [Modernize your help files with HelpNDoc's WinHelp HLP to CHM conversion tool](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
