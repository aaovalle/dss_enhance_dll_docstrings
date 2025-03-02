# ParserV (Variant) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

void ParserV(int32\_t Parameter, uintptr\_t \*Pointer, int32\_t \*Type, int32\_t \*Size);

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

### Parameter 0: Parser.Vector

This parameter returns token as pointer to an array of doubles. For parsing quoted array syntax. The caller must specify in the argument "Size"  the expected vector length.

&nbsp;

### Parameter 1: Parser.Matrix

Use this property to parse a Matrix token in OpenDSS format. Returns a pointer to an array of doubles containing the square matrix of order specified in the argument "Size". Order same as default fortran order: column by column. The caller must specify the order in the argument "Size".

&nbsp;

### Parameter 2: Parser.SymMatrix

Use this property to parse a Matrix token in lower triangular form. Symmetry is forced. Returns a pointer to an array of doubles containing the square matrix of order specified in the argument "Size". Order same as default fortran order: column by column. The caller must specify the  order in the argument "Size".


***
_Created with the Standard Edition of HelpNDoc: [Don't be left in the past: convert your WinHelp HLP help files to CHM with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
