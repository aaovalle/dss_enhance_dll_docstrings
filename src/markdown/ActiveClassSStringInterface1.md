# ActiveClassS (String) Interface

&nbsp;

This interface can be used to read/modify the properties of the ActiveClass Class where the values are strings. The structure of the interface is as follows:

&nbsp;

CStr ActiveClassI(int32\_t Parameter, CStr argument);

&nbsp;

This interface returns a string, the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: ActiveClass.Name read

This parameter gets the name of the active Element of the Active class.

&nbsp;

### Parameter 1: ActiveClass.Name write

This parameter sets the name of the active Element of the Active class.

&nbsp;

### Parameter 2: ActiveClass.ActiveClassName

This parameter sets the name of the active Element of the Active class.

&nbsp;

### Parameter 3: ActiveClass.ActiveClassParent

This parameter returns the name of the parent class of the Active class.


***
_Created with the Standard Edition of HelpNDoc: [Keep Your Sensitive PDFs Safe with These Easy Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
