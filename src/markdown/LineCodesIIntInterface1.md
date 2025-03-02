# LineCodesI (Int) Interface

&nbsp;

This interface can be used to read/modify the properties of the LineCode Class where the values are integers. The structure of the interface is as follows:

&nbsp;

int32\_t LineCodesI(int32\_t Parameter, int32\_t argument)

&nbsp;

This interface returns an integer (signed 32 bits), the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: LineCodes.Count

This parameter gets the number of Line Objects in Active Circuit.

&nbsp;

### Parameter 1: LineCodes.First

This parameter sets the first element active. Returns 0 if no lines. Otherwise, index of the line element.

&nbsp;

### Parameter 2: LineCodes.Next

This parameter sets the next element active. Returns 0 if no lines. Otherwise, index of the line element.

&nbsp;

### Parameter 3: LineCodes.Units Read

This parameter delivers the units of the active LineCode as an integer.

&nbsp;

### Parameter 4: LineCodes.Units Write

This parameter sets the units of the active LineCode. The units must be specified as an integer in the argument. Please refer to the OpenDSS User manual for more information.

&nbsp;

### Parameter 5: LineCodes.Phasess Read

This parameter delivers the number of phases of the active LineCode as an integer.

&nbsp;

### Parameter 6: LineCodes.Phasess Write

This parameter sets the number of phases of the active LineCode. The units must be specified as an integer in the argument. 

&nbsp;

### Parameter 7: Lines. IsZ1Z0

This parameter gets the flag (Boolean 1/0) denoting whether the impedance data were entered in symmetrical components.


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create High-Quality Documentation with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
