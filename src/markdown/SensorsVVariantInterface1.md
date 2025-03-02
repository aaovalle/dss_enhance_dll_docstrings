# SensorsV (Variant) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

void SensorsV(int32\_t Parameter, uintptr\_t \*Pointer, int32\_t \*Type, int32\_t \*Size);

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

### Parameter 0: Sensors.AllNames

This parameter returns a pointer to an array of bytes containing the names of all the existing sensors in the project. Each string is separated by a NULL (0) character.

&nbsp;

### Parameter 1: Sensors.Currents read

This parameter returns a pointer to an array of doubles containing the values for the line current measurements; don't use with KWS and KVARS.

&nbsp;

### Parameter 2: Sensors.Currents write

This parameter allows to write the array of line current measurements (doubles) for the active sensor object using the given pointer. The argument Pointer must be provided by the caller pointing to an array of doubles containing the new data. The argument mySize must also contain the length of the array of doubles; don't use with KWS and KVARS.

&nbsp;

### Parameter 3: Sensors.KVARS read

This parameter returns a pointer to an array of doubles containing the values for Q measurements; overwrites currents with a new estimate using KWS.

&nbsp;

### Parameter 4: Sensors.KVARS write

This parameter allows to write the array of Q measurements (doubles) for the active sensor object using the given pointer. The argument Pointer must be provided by the caller pointing to an array of doubles containing the new data. The argument mySize must also contain the length of the array of doubles; overwrites currents with a new estimate using KWS.

&nbsp;

### Parameter 5: Sensors.KWS read

This parameter returns a pointer to an array of doubles containing the values for P measurements; overwrites currents with a new estimate using KVARS.

&nbsp;

### Parameter 6: Sensors.KWS write

This parameter allows to write the array of P measurements (doubles) for the active sensor object using the given pointer. The argument Pointer must be provided by the caller pointing to an array of doubles containing the new data. The argument mySize must also contain the length of the array of doubles; overwrites currents with a new estimate using KVARS.

&nbsp;

### Parameter 7: Sensors.AllocationFactor

This parameter returns a pointer to an array of doubles containing the allocation factors per phase for the active sensor.


***
_Created with the Standard Edition of HelpNDoc: [Make Documentation a Breeze with HelpNDoc's Clean and Efficient User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
