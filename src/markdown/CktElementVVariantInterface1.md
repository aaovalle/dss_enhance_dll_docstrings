# CktElementV (Variant) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

void CktElementV(int32\_t Parameter, uintptr\_t \*Pointer, int32\_t \*Type, int32\_t \*Size);

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

### Parameter 0: CktElement.BusNames - read

This parameter delivers a pointer to an array of strings with the names of all the buses connected to the active circuit element. The names of the elements are separated by a NULL (0) character.

&nbsp;

### Parameter 1: CktElement.BusNames - write

This parameter allows to fix an array of strings with the names of all the buses connected to the active circuit element. The argument Pointer must be provided by the caller pointing to an array of Bytes containing the array of strings with the bus names. Each name must be separated within the array by a NULL (0) character. As a result, this command will return the number of bytes read and successfully written in the argument "Size".

&nbsp;

### Parameter 2: CktElement.Voltages

This parameter returns a pointer to an array of complex with the voltages at terminals of the active circuit element. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 3: CktElement.Currents

This parameter returns a pointer to an array of complex with the currents at terminals of the active circuit element. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 4: CktElement.powers

This parameter returns a pointer to an array of complex with the powers at terminals of the active circuit element. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 5: CktElement.Losses

This parameter returns a pointer to an array of complex with the Losses at terminals of the active circuit element. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 6: CktElement.PhaseLosses

This parameter returns a pointer to an array of complex with the Losses per phase at the terminals of the active circuit element. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 7: CktElement.SeqVoltages

This parameter returns a pointer to an array of doubles with the symmetrical component voltages per phase at the terminals of the active circuit element.

&nbsp;

### Parameter 8: CktElement.SeqCurrents

This parameter returns a pointer to an array of doubles with the symmetrical component Currents per phase at the terminals of the active circuit element.

&nbsp;

### Parameter 9: CktElement.SeqPowers

This parameter returns a pointer to an array of complex with the symmetrical component powers per phase at the terminals of the active circuit element. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 10: CktElement.AllPropertyNames

This parameter returns a pointer to an array of strings with the names of all the properties of the active circuit element. The names of the elements are separated by a NULL (0) character.

&nbsp;

### Parameter 11: CktElement.Residuals

This parameter returns a pointer to an array of complex with the residual currents (magnitude, angle) in all the nodes of the active circuit element.  Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 12: CktElement.YPrim

This parameter returns a pointer to an array of complex with the Y primitive matrix of the active circuit element. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 13: CktElement.CplxSeqVoltages

This parameter returns a pointer to an array of complex with the sequence voltages for all terminals of the active circuit element. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 14: CktElement.CplxSeqCurrents

This parameter returns a pointer to an array of complex with the sequence currents for all terminals of the active circuit element.  Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 15: CktElement.AllVariableNames

This parameter returns a pointer to an array of strings listing all the published state variable names, if the active circuit element is a PCElement. Otherwise, null string. The names of the elements are separated by a NULL (0) character.

&nbsp;

### Parameter 16: CktElement.AllVariableValues

This parameter returns a pointer to an array of doubles listing all the values of the state variables, if the active circuit element is a PCElement. Otherwise, 0 value.

&nbsp;

### Parameter 17: CktElement.Nodeorder

This parameter returns a pointer to an array integers containing the node numbers (representing phases, for example) for each conductor of each terminal.

&nbsp;

### Parameter 18: CktElement.CurrentsMagAng

This parameter returns a pointer to an array of complex containing the currents in magnitude, angle format for the active circuit element. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 19: CktElement.VoltagesMagAng

This parameter returns a pointer to an array of complex containing the voltages in magnitude, angle format for the active circuit element.  Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 20: CktElement.TotalPowers

Returns a pointer to an array of complex with the the total powers (complex) at ALL terminals of the active circuit element. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).


***
_Created with the Standard Edition of HelpNDoc: [Free PDF documentation generator](<https://www.helpndoc.com>)_
