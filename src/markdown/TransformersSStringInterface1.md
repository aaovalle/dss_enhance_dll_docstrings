# TransformersS (String) Interface

&nbsp;

This interface can be used to read/modify the properties of the Transformers Class where the values are Strings. The structure of the interface is as follows:

&nbsp;

CStr TransformersS(int32\_t Parameter, CStr argument) ;

&nbsp;

This interface returns a string, the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: Transformers.XfmrCode read

This parameter gets the name of an XfrmCode that supplies electrical parameters for this transformer.

&nbsp;

### Parameter 1: Transformers.XfmrCode write

This parameter sets the name of an XfrmCode that supplies electrical parameters for this transformer.

&nbsp;

### Parameter 2: Transformers.Name read

This parameter gets the active transformer name.

&nbsp;

### Parameter 3: Transformers.Name write

This parameter sets the active transformer by name

&nbsp;

### Parameter 4: Transformers.StrWdgVoltages

This parameter gets the voltages at the active winding of the active transformer in string format.


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Convert Your Word Doc to an eBook: A Step-by-Step Guide](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
