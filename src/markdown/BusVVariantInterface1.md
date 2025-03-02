# BusV (Variant) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

void  BUSV(int32\_t Parameter, uintptr\_t \*Pointer, int32\_t \*Type, int32\_t \*Size);

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

### Parameter 0: Bus.Voltages

This parameter returns a pointer to a complex array of voltages at this bus. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per data).

&nbsp;

### Parameter 1: Bus.SeqVoltages

This parameter returns a pointer to an array of doubles containing the Sequence voltages at this bus.

&nbsp;

### Parameter 2: Bus.Nodes

This parameter returns a pointer to an array of integer containing the node numbers defined at the bus in same order as the voltages.

&nbsp;

### Parameter 3: Bus.Voc

This parameter returns a pointer to an array of complex containing the open circuit voltage for the active bus. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 4: Bus.Isc

This parameter returns a pointer to an array of complex containing the short circuit current for the active bus. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 5: Bus.PuVoltages

This parameter returns a pointer to an array of complex containing the voltages in per unit at the active bus. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

### &nbsp;

### Parameter 6: Bus.ZscMatrix

This parameter returns a pointer to an array of complex containing the Zsc matrix at the active bus, column by column. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 7: Bus.Zsc1

This parameter returns a pointer to the complex positive-sequence short circuit impedance at bus. The element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

### &nbsp;

### Parameter 8: Bus.Zsc0

This parameter returns a pointer to the complex zero-sequence short circuit impedance at bus. The element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

### &nbsp;

### Parameter 9: Bus.YscMatrix

This parameter returns a pointer to an array of complex containing the Ysc matrix at the active bus, column by column. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

### &nbsp;

### Parameter 10: Bus.CplxSeqVoltages

This parameter returns a pointer to an array of complex containing the sequence voltages (0, 1, 2) at the active bus. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 11: Bus.VLL

This parameter for 2 and 3 phase buses, returns a pointer to an array of complex numbers representing L-L voltages in volts. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only first 3. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 12: Bus.PuVLL

This parameter for 2 and 3 phase buses, returns a pointer to an array of complex numbers representing L-L voltages in per unit. Returns -1.0 for 1-phase bus. If more than 3 phases, returns only first 3. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 13: Bus.VMagAngle

This parameter returns a pointer to an array of complex containing voltages in magnitude (VLN), angle (deg). Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 14: Bus.PuVMagAngle

This parameter returns a variant array of doubles containing voltages in per unit and angles in degrees.

&nbsp;

### Parameter 15: Bus.LineList

This parameter returns a pointer to an array of strings containing the names of the lines connected to the active bus. The names of the lines include the class name “Line.”.

&nbsp;

### Parameter 16: Bus.LoadList

This parameter returns a pointer to an array of strings containing the names of the loads connected to the active bus. The names of the lines include the class name “Load.”.

&nbsp;

### Parameter 17: Bus.ZSC012 Matrix

Returns a pointer to an array of doubles containing the complete 012 Zsc matrix.

&nbsp;

### Parameter 18: Bus.AllPCEatBus

Returns a pointer to an array of strings (Char) with the names of all PCE connected to the active bus.

&nbsp;

### Parameter 19: Bus.AllPDEatBus

Returns a pointer to an array of strings (Char) with the names of all PDE connected to the active bus.


***
_Created with the Standard Edition of HelpNDoc: [Produce electronic books easily](<https://www.helpndoc.com/create-epub-ebooks>)_
