# ReactorsV (Variant) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

void ReactorsV(int32\_t Parameter, uintptr\_t \*Pointer, int32\_t \*Type, int32\_t \*Size);

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

### Parameter 0: Reactors.AllNames

This parameter returns a pointer to an array of bytes containing the names of all the existing WindGens in the project. Each string is separated by a NULL (0) character.

&nbsp;

### Parameter 1: Reactors.RMatrix read

Gets the Resistance matrix, lower triangle, ohms at base frequency for the active reactor.

&nbsp;

### Parameter 2: Reactors.RMatrix write

Sets the Resistance matrix, lower triangle, ohms at base frequency for the active reactor.

&nbsp;

### Parameter 3: Reactors.XMatrix read

Gets the Inductance matrix, lower triangle, ohms at base frequency for the active reactor.

&nbsp;

### Parameter 4: Reactors.XMatrix write

Sets the Inductance matrix, lower triangle, ohms at base frequency for the active reactor.

&nbsp;

### Parameter 5: Reactors.Z read

Alternative way of getting R and X properties for the active reactor using a 2-element array of doubles.

&nbsp;

### Parameter 6: Reactors.Z write

Alternative way of setting R and X properties for the active reactor using a 2-element array of doubles.

&nbsp;

### Parameter 7: Reactors.Z0 read

Gets the Zer0-sequence impedance, ohms, as a 2-element array representing a complex number for the active reactor.

&nbsp;

### Parameter 8: Reactors.Z0 write

Sets the Zer0-sequence impedance, ohms, as a 2-element array representing a complex number for the active reactor.

&nbsp;

### Parameter 9: Reactors.Z1 read

Gets the Positive-sequence impedance, ohms, as a 2-element array representing a complex number for the active reactor.

&nbsp;

### Parameter 10: Reactors.Z1 write

Sets the Positive-sequence impedance, ohms, as a 2-element array representing a complex number for the active reactor.

&nbsp;

### Parameter 11: Reactors.Z2 read

Gets the Negative-sequence impedance, ohms, as a 2-element array representing a complex number for the active reactor.

&nbsp;

### Parameter 12: Reactors.Z2 write

Sets the Negative-sequence impedance, ohms, as a 2-element array representing a complex number for the active reactor.

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create High-Quality Documentation with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
