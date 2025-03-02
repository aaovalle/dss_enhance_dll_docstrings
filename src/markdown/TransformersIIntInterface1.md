# TransformersI (Int) Interface

&nbsp;

This interface can be used to read/modify the properties of the Transformers Class where the values are integers. The structure of the interface is as follows:

&nbsp;

int32\_t TransformersI(int32\_t Parameter, int32\_t argument) ;

&nbsp;

This interface returns an integer (signed 32 bits), the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: Transformers.NumWindings read

This parameter gets the number of windings on this transformer. Allocates memory; set or change this property first.

&nbsp;

### Parameter 1: Transformers.NumWindings write

This parameter sets the number of windings on this transformer. Allocates memory; set or change this property first.

&nbsp;

### Parameter 2: Transformers.Wdg read

This parameter gets the active winding number from 1..NumWindings. Update this before reading or setting a sequence of winding properties (R, Tap, kV, kVA, etc.).

&nbsp;

### Parameter 3: Transformers.Wdg write

This parameter sets the active winding number from 1..NumWindings. Update this before reading or setting a sequence of winding properties (R, Tap, kV, kVA, etc.).

&nbsp;

### Parameter 4: Transformers.NumTaps read

This parameter gets the active winding number of tap steps between MinTap and MaxTap.

&nbsp;

### Parameter 5: Transformers.NumTaps write

This parameter sets the active winding number of tap steps between MinTap and MaxTap.

&nbsp;

### Parameter 6: Transformers.IsDelta read

This parameter gets the information about if the active winding is delta (1) or wye (0) connection.

&nbsp;

### Parameter 7: Transformers.IsDelta write

This parameter sets the information about if the active winding is delta (1) or wye (0) connection.

&nbsp;

### Parameter 8: Transformers.First

This parameter sets the first Transformer active. Return 0 if no more.

&nbsp;

### Parameter 9: Transformers.Next

This parameter sets the next Transformer active. Return 0 if no more.

&nbsp;

### Parameter 10: Transformers.Count

This parameter gets the number of transformers within the active circuit.

&nbsp;

### Parameter 11: Transformers.CoreType read

This parameter gets the code for the core type of the active transformer.

&nbsp;

### Parameter 12: Transformers.CoreType write

This parameter sets the code for the core type of the active transformer using the value given by the user in the argument.


***
_Created with the Standard Edition of HelpNDoc: [Free Kindle producer](<https://www.helpndoc.com/feature-tour/create-ebooks-for-amazon-kindle>)_
