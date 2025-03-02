# DSSElementI (Int) Interface

&nbsp;

This interface can be used to read/modify the properties of the DSSElement Class where the values are integers. The structure of the interface is as follows:

&nbsp;

int32\_t DSSElementI(int32\_t Parameter, int32\_t argument) ;

&nbsp;

This interface returns an integer (signed 32 bits), the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: DSSElement.NumProperties

This parameter gets the number of properties for the active DSS object.


***
_Created with the Standard Edition of HelpNDoc: [Easy Qt Help documentation editor](<https://www.helpndoc.com>)_
