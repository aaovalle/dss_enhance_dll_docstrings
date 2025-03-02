# LineCodesF (Float) Interface

&nbsp;

This interface can be used to read/modify the properties of the LineCode Class where the values are doubles. The structure of the interface is as follows:

&nbsp;

double LineCodesF(int32\_t Parameter, double argument)

&nbsp;

This interface returns a floating point number, the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: LineCodes.R1 read

This parameter gets the Positive-sequence resistance in ohms per unit length for the active LineCode.

&nbsp;

### Parameter 1: LinesCode.R1 write

This parameter sets the Positive-sequence resistance in ohms per unit length for the active LineCode. This value must be specified in the argument as a double.

&nbsp;

### Parameter 2: LineCodes.X1 read

This parameter gets the Positive-sequence reactance in ohms per unit length for the active LineCode.

&nbsp;

### Parameter 3: LinesCode.X1 write

This parameter sets the Positive-sequence reactance in ohms per unit length for the active LineCode. This value must be specified in the argument as a double.

&nbsp;

### Parameter 4: LineCodes.R0 read

This parameter gets the Zero-sequence resistance in ohms per unit length for the active LineCode.

&nbsp;

### Parameter 5: LinesCode.R0 write

This parameter sets the Zero-sequence resistance in ohms per unit length for the active LineCode. This value must be specified in the argument as a double.

&nbsp;

### Parameter 6: LineCodes.X0 read

This parameter gets the Zero-sequence reactance in ohms per unit length for the active LineCode.

&nbsp;

### Parameter 7: LinesCode.X0 write

This parameter sets the Zero-sequence reactance in ohms per unit length for the active LineCode. This value must be specified in the argument as a double.

&nbsp;

### Parameter 8: LineCodes.C1 read

This parameter gets the Positive-sequence capacitance in ohms per unit length for the active LineCode.

&nbsp;

### Parameter 9: LinesCode.C1 write

This parameter sets the Positive-sequence capacitance in ohms per unit length for the active LineCode. This value must be specified in the argument as a double.

&nbsp;

### Parameter 10: LineCodes.C0 read

This parameter gets the Zero-sequence capacitance in ohms per unit length for the active LineCode.

&nbsp;

### Parameter 11: LinesCode.C0 write

This parameter sets the Zero-sequence capacitance in ohms per unit length for the active LineCode. This value must be specified in the argument as a double.

&nbsp;

### Parameter 12: LineCodes.NormAmps read

This parameter gets the normal ampere rating for the active LineCode.

&nbsp;

### Parameter 13: LinesCode.NormAmps write

This parameter sets the normal ampere rating for the active LineCode. This value must be specified in the argument as a double.

&nbsp;

### Parameter 14: LineCodes.EmergAmps read

This parameter gets the Emergency ampere rating for the active LineCode.

&nbsp;

### Parameter 15: LinesCode.EmergAmps write

This parameter sets the Emergency ampere rating for the active LineCode. This value must be specified in the argument as a double.


***
_Created with the Standard Edition of HelpNDoc: [Easily share your documentation with the world through a beautiful website](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
