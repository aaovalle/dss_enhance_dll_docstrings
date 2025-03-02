# LinesV (Variant) Interface

&nbsp;

This interface can be used to read/modify the properties of the Lines Class where the values are array-based. The structure of the interface is as follows:

&nbsp;

void LinesV(int32\_t Parameter, uintptr\_t \*Pointer, int32\_t \*Type, int32\_t \*Size);

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

### Parameter 0: Lines.AllNames

This parameter returns a pointer to an array of bytes containing the names of all the existing Lines in the project. Each string is separated by a NULL (0) character.

&nbsp;

### Parameter 1: Lines.RMatrix read

This parameter returns a pointer to an array of doubles with the resistance matrix (full), ohms per unit length. 

&nbsp;

### Parameter 2: Lines.RMatrix write

This parameter sets the resistance matrix in ohms per unit length of the active Line using the given pointer. The argument Pointer must be provided by the caller pointing to an array of doubles containing the new data.

&nbsp;

### Parameter 3: Lines.XMatrix read

This parameter returns a pointer to an array of doubles with the reactance matrix (full), ohms per unit length.

&nbsp;

### Parameter 4: Lines.XMatrix write

This parameter sets the reactance matrix in ohms per unit length of the active Line using the given pointer. The argument Pointer must be provided by the caller pointing to an array of doubles containing the new data.

&nbsp;

### Parameter 5: Lines.CMatrix read

This parameter returns a pointer to an array of doubles with the capacitance matrix (full), nanofarads per unit length. 

&nbsp;

### Parameter 6: Lines.CMatrix write

This parameter sets the capacitance matrix in ohms per unit length of the active Line using the given pointer. The argument Pointer must be provided by the caller pointing to an array of doubles containing the new data. 

&nbsp;

### Parameter 7: Lines.YPrim read

This parameter returns a pointer to an array of complex with the YPrimitive of the active Line. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 8: Lines.YPrim write

This parameter does nothing at present.

***
_Created with the Standard Edition of HelpNDoc: [Protect Your Confidential PDFs with These Simple Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
