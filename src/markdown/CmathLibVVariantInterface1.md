# CmathLibV (Variant) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

void CmathLibV(int32\_t Parameter, uintptr\_t \*Pointer, int32\_t \*Type, int32\_t \*Size);

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

### Parameter 0: CmathLib.cmplx

This parameter returns a pointer to the complex number resulting of combining 2 numbers provided as an array of doubles. The caller must provide the argument Pointer pointing to the array of doubles containing the data. Once the operation has completed, the Pointer argument will be updated to point to the complex number created. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 1: CmathLib.ctopolardeg

This parameter converts the given complex number to magnitude and angle, degrees. Returns a pointer to an complex representing the equivalent polar representation. The caller must provide the argument Pointer pointing to the array of complex (size 1) containing the data. Once the operation has completed, the Pointer argument will be updated to point to the complex number created. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 2: CmathLib.pdegtocomplex

This parameter converts the given magnitude, angle in degrees into its equivalent complex number. Returns a pointer to an complex representing the equivalent complex representation. The caller must provide the argument Pointer pointing to the array of complex (size 1) containing the data. Once the operation has completed, the Pointer argument will be updated to point to the complex number created. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).


***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Simplicity of HelpNDoc's User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
