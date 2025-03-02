# IsourcesS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr IsourcesS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Isources.Name read

This parameter gets the name of the active Isource object.

&nbsp;

**Parameter 1: Isources.Name write**

This parameter sets the name of the active Isource object.


***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Documentation with HelpNDoc's Project Analyzer Features](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
