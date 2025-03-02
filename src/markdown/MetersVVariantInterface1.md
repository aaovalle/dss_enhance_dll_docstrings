# MetersV (Variant) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

void  MetersV(int32\_t Parameter, uintptr\_t \*Pointer, int32\_t \*Type, int32\_t \*Size);

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

### Parameter 0: Meters.AllNames

This parameter returns a pointer to an array of bytes containing the names of all the existing Energy Meter in the project. Each string is separated by a NULL (0) character.

&nbsp;

### Parameter 1: Meters.RegisterNames

This parameter returns a pointer to an array of bytes containing the names of the registers within the active energy meter. Each string is separated by a NULL (0) character.

&nbsp;

### Parameter 2: Meters.RegisterValues

This parameter returns a pointer to an array of doubles containing the values in the Meter registers for the active Meter.

&nbsp;

### Parameter 3: Meters.Totals

This parameter returns a pointer to an array of doubles containing the totals for all registers of all Meters.

&nbsp;

### Parameter 4: Meters.PeakCurrent read

This parameter returns a pointer to an array of doubles containing the Peak Current Property for the active Energy meter.

&nbsp;

### Parameter 5: Meters.PeakCurrent Write

This parameter sets the Peak Current multipliers of the active Energy meter using the given pointer. The argument Pointer must be provided by the caller pointing to an array of doubles containing the new data.The argument mySize must also contain the length of the array of doubles.

&nbsp;

### Parameter 6: Meters.CalCurrent read

This parameter returns a pointer to an array of doubles containing the magnitude of the real part of the Calculated Current (normally determined by solution) for the meter to force some behavior on Load Allocation.

&nbsp;

### Parameter 7: Meters.CalcCurrent Write

This parameter sets the magnitude of the real part of the Calculated Current (normally determined by solution) of the active Energy meter using the given pointer  to force some behavior on Load Allocation. The argument Pointer must be provided by the caller pointing to an array of doubles containing the new data.The argument mySize must also contain the length of the array of doubles.

&nbsp;

### Parameter 8: Meters.AllocFactors read

This parameter returns a pointer to an array of doubles containing the allocation factors for the active Meter.

&nbsp;

### Parameter 9: Meters. AllocFactors Write

This parameter sets the phase allocation factors of the active Energy meter using the given pointer. The argument Pointer must be provided by the caller pointing to an array of doubles containing the new data.The argument mySize must also contain the length of the array of doubles.

&nbsp;

### Parameter 10: Meters.AllEndElements

This parameter returns a pointer to an array of bytes containing the names of all zone end elements of the active energy meter. Each string is separated by a NULL (0) character.

&nbsp;

### Parameter 11: Meters.AllBranchesInZone

This parameter returns a pointer to an array of bytes containing the names of all branches in zone of the active energy meter. Each string is separated by a NULL (0) character.

&nbsp;

### Parameter 12: Meters.AllPCEinZone

This parameter returns a pointer to an array of bytes containing the names of all PCE in zone of the active energy meter. Each string is separated by a NULL (0) character.


***
_Created with the Standard Edition of HelpNDoc: [Converting Word Docs to eBooks Made Easy with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
