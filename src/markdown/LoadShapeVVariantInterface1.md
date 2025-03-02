# LoadShapeV (Variant) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

void LoadShapeV(int32\_t Parameter, uintptr\_t \*Pointer, int32\_t \*Type, int32\_t \*Size);

&nbsp;

In this version of the DLL the API requires 4 arguments Some of these arguments are informative while others provide data access through memory address. This avoids creating unnecessary copies of the same data across the system. The 4 arguments used in this API are:

&nbsp;

* Parameter: Indicates the data array that wants to be accessed/written.
* Pointer: Is the pointer to the array structure.
* Type: Is the type of data contained in the structure, it can be one of: 0 - Boolean, 1- Integer (32 bit), 2- double (64 bit), 3- Complex, 4- String.
* Size: Is the size in Bytes of the structure, it only considers the elements inside the structure without the identifiers added by DSS. In the case of array of strings includes the null byte (0) between the elements of the array.  

&nbsp;

The return values depend on the given Parameter, which can be one of the following:

&nbsp;

### Parameter 0: LoadShapes.AllNames

This parameter returns a pointer to an array of bytes containing the names of all the existing Load shapes in the project. Each string is separated by a NULL (0) character.

&nbsp;

### Parameter 1: LoadShapes.PMult read

This parameter returns a pointer to an array of doubles with the active power (P) multipliers of the active LoadShape object. 

&nbsp;

### Parameter 2: LoadShapes.PMult write

This parameter sets the active power (P) multipliers of the active LoadShape using the given pointer. The argument Pointer must be provided by the caller pointing to an array of doubles containing the new data.The argument mySize must also contain the length of the array of doubles.

&nbsp;

### Parameter 3: LoadShapes.QMult read

This parameter returns a pointer to an array of doubles with the reactive power (Q) multipliers of the active LoadShape object. 

&nbsp;

### Parameter 4: LoadShapes.QMult write

This parameter sets the reactive power (Q) multipliers of the active LoadShape using the given pointer. The argument Pointer must be provided by the caller pointing to an array of doubles containing the new data.The argument mySize must also contain the length of the array of doubles.

&nbsp;

### Parameter 5: LoadShapes.TimeArray read

This parameter returns a pointer to an array of doubles with the hours corresponding to P and Q multipliers when the Interval = 0, of the active LoadShape object.

&nbsp;

### Parameter 6: LoadShapes.TimeArray write

This parameter sets a time array in hours corresponding to P and Q multipliers when the Interval = 0.


***
_Created with the Standard Edition of HelpNDoc: [Free HTML Help documentation generator](<https://www.helpndoc.com>)_
