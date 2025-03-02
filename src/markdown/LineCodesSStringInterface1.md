# LineCodesS (String) Interface

&nbsp;

This interface can be used to read/modify the properties of the LineCode Class where the values are Strings. The structure of the interface is as follows:

&nbsp;

CStr LineCodesS(int32\_t Parameter, CStr argument)

&nbsp;

This interface returns a string, the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: LineCodes.Name read

This parameter gets the name of the active LineCode element.

&nbsp;

### Parameter 1: LineCodes.Name write

This parameter sets the name of the active LineCode element. The new value must be specified in the argument as a string.


***
_Created with the Standard Edition of HelpNDoc: [Transform Your Documentation Process with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
