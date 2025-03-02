# CapacitorsV (Array) Interface

&nbsp;

This interface can be used to read/modify the properties of the Capacitors Class where the values are array-based. The structure of the interface is as follows:

&nbsp;

void  CapacitorsV(int32\_t Parameter, uintptr\_t \*Pointer, int32\_t \*Type, int32\_t \*Size);

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

### Parameter 0: Capacitors.AllNames

This parameter gets a pointer to an array of bytes with all Capacitor names in the circuit, the bytes correspond to characters representing the array of strings within DSS containing the names of all the elements within this class. The names of the elements are separated by a NULL (0) character.

&nbsp;

### Parameter 1: Capacitors.States read

This parameter gets a variant array of integers \[0..numsteps-1\] indicating the state of each step. If value is -1 and error has occurred. In this case Pointer is the pointer to the array of integers within DSS containing the states of the active capacitor.

&nbsp;

### Parameter 2: Capacitors.States write

This parameter sets a variant array of integers \[0..numsteps-1\] indicating the state of each step. If value is -1 and error has occurred.In this case the argument Pointer works as input indicating the pointer to the array of integers located at the caller memory containing the states (integers) to be used for setting he new states of the active capacitor.


***
_Created with the Standard Edition of HelpNDoc: [Generate Kindle eBooks with ease](<https://www.helpndoc.com/feature-tour/create-ebooks-for-amazon-kindle>)_
