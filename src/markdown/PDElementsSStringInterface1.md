# PDElementsS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr PDElementsF(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: PDElements.Name read

This parameter gets the name of the active PDElement, returns null string if active element id not PDElement.

&nbsp;

### Parameter 1: PDElements.Name write

This parameter sets the name of the active PDElement, returns null string if active element id not PDElement.


***
_Created with the Standard Edition of HelpNDoc: [HelpNDoc's Project Analyzer: Incredible documentation assistant](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
