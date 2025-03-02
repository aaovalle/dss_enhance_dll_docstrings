# StoragesV (Variant) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

void StoragesV(int32\_t Parameter, uintptr\_t \*Pointer, int32\_t \*Type, int32\_t \*Size);

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

### Parameter 0: Storages.AllNames

This parameter returns a pointer to an array of bytes containing the names of all the existing Storage in the project. Each string is separated by a NULL (0) character.

&nbsp;

### Parameter 1: Storages.RegisterNames

This parameter returns a pointer to an array of bytes containing the names of all the energy registers of the active Storage. Each string is separated by a NULL (0) character.

&nbsp;

### Parameter 2: Storages.RegisterValues

This parameter returns a pointer to an array of doubles containing the values of all the energy registers of the active Storage. Each string is separated by a NULL (0) character.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Convert Your Word Doc to an eBook: A Step-by-Step Guide](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
