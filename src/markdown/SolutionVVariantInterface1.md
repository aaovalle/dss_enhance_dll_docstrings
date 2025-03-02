# SolutionV (Variant) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

void  SolutionV(int32\_t Parameter, uintptr\_t \*Pointer, int32\_t \*Type, int32\_t \*Size);

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

### Parameter 0: Solution.EventLog

This parameter returns a pointer to an array of bytes containing the EventLog after a successful simulation. Each string is separated by a NULL (0) character.

&nbsp;

### Parameter 1: Solution.IncMatrix

This parameter returns a pointer to an array of integers containing the incidence matrix (1-D). Each cell of the incidence matrix is delivered using 3 elements of the array delivered, the first is the row, the second is the column and the third is the value (1/-1). This procedure will only deliver the non-zero elements.

&nbsp;

### Parameter 2: Solution.BusLevels

This parameter returns a pointer to an array of integers containing BusLevels array. This array gives a numeric value to each bus to specify how far it is from the circuit’s backbone (a continuous path from the feeder head to the feeder end). It is very handy to understand the circuit’s topology.

&nbsp;

### Parameter 3: Solution.IncMatrixRows

This parameter returns a pointer to an array of bytes containing the names of the rows of the incidence matrix (PDElements), depending on the way the Branch to node incidence matrix was calculated (CalcIncMatrix/CalcIncMatrix\_O) the result could be very different.

&nbsp;

### Parameter 4: Solution.IncMatrixCols

This parameter returns  a pointer to an array of bytes containing the names of the cols of the incidence matrix (buses), depending on the way the Branch to node incidence matrix was calculated (CalcIncMatrix/CalcIncMatrix\_O) the result could be very different.

&nbsp;

### Parameter 5: Solution.Laplacian

This parameter returns a pointer to an array of integers containing the Laplacian matrix using the incidence matrix previously calculated, this means that before calling this command the incidence matrix needs to be calculated using calcincmatrix/calcincmatrix\_o. This command will return only the non-zero values in compressed coordinate format (row, col, value).


***
_Created with the Standard Edition of HelpNDoc: [Free help authoring environment](<https://www.helpndoc.com/help-authoring-tool>)_
