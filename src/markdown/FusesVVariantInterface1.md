# FusesV (Variant) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

void FusesV(int32\_t Parameter, uintptr\_t \*Pointer, int32\_t \*Type, int32\_t \*Size);

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

### Parameter 0: Fuses.AllNames

This parameter returns a pointer to an array of string containing names of all fuses in the circuit. Each string is separated by a NULL (0) character.

&nbsp;

### Parameter 1: Fuses.States - read

This property a pointer to an array of strings representing the present state of each phase of the fuse. Each string is separated by a NULL (0) character.

&nbsp;

### Parameter 2: Fuses.States - write

This property sets the present state per phase through an array of strings. Each string must specify the state with a string "Closed" or "Open". The argument Pointer must be provided by the caller pointing to an array of Bytes containing the array of strings with the state per phase. Each string must be separated within the array by a NULL (0) character. As a result, this command will return the number of Bytes read and successfully written in the argument "Size". 

&nbsp;

### Parameter 3: Fuses.NormalState - read

This property a pointer to an array of strings representing the normal state of each phase of the fuse. Each string is separated by a NULL (0) character.

&nbsp;

### Parameter 4: Fuses.NormalState - write

This property sets the normal state per phase through an array of strings. Each string must specify the state with a string "Closed" or "Open". The argument Pointer must be provided by the caller pointing to an array of Bytes containing the array of strings with the state per phase. Each string must be separated within the array by a NULL (0) character. As a result, this command will return the number of Bytes read and successfully written in the argument "Size".

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Word Document into a Professional eBook with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
