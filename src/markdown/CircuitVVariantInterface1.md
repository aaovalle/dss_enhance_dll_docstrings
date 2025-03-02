# CircuitV (Variant) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

void  CircuitV(int32\_t Parameter, uintptr\_t \*Pointer, int32\_t \*Type, int32\_t \*Size);

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

### Parameter 0: Circuit.Losses

This parameter returns a pointer to an array of complex with the total losses of the active circuit. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 1: Circuit.LineLosses

This parameter returns a pointer to an array of complex with the total Line losses of the active circuit. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 2: Circuit.SubstationLosses

This parameter returns a pointer an array of complex with the total transformer losses of the active circuit. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 3: Circuit.TotalPower

This parameter returns a pointer to an array of complex with the total power in watts delivered to the active circuit. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 4: Circuit.AllBusVolts

This parameter returns a pointer to an array of complex with the node voltages from the most recent solution. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 5: Circuit.AllBusVMag

This parameter returns a pointer to an array of doubles with the node voltages from the most recent solution.

&nbsp;

### Parameter 6: Circuit.AllElementNames

This parameter returns a pointer to an array of strings with the names of all the elements of the active circuit. The names of the elements are separated by a NULL (0) character.

&nbsp;

### Parameter 7: Circuit.AllBusNames

This parameter returns a pointer to an array of Bytes with the names of all the Buses of the active circuit (See AllNodeNames). Argument2 must be 0.

&nbsp;

### Parameter 8: Circuit.AllElementLosses

This parameter returns a pointer to an array of complex with the losses in each element of the active circuit. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 9: Circuit.AllBusVMagPu

This parameter returns a pointer to an array of doubles with the voltages in per unit of the most recent solution of the active circuit.

&nbsp;

### Parameter 10: Circuit.AllNodeNames

This parameter returns an array of strings containing full name of each node in system in same order as returned by AllBusVolts, etc. Argument2 must be 0.

&nbsp;

### Parameter 11: Circuit.SystemY

This parameter returns a pointer to an array of complex containing the Y Bus Matrix of the system (after a solution has been performed). Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 12: Circuit.AllBusDistances

This parameter returns a pointer to an array of doubles with the distance from each bus to its parent EnergyMeter. Corresponds to sequence in AllBusNames. 

&nbsp;

### Parameter 13: Circuit.AllNodeDistances

This parameter returns a pointer to an array of doubles with the distance from the each pointed Node to its parent EnergyMeter. Corresponds to sequence in AllBusVmag.

&nbsp;

### Parameter 14: Circuit.AllNodeVMagbyPhase

This parameter returns a pointer to an array of doubles representing the voltage magnitudes for nodes on the specified phase. The argument Pointer must specify the pointer to the integer containing the phase number when called, the Pointer argument will update when returning results with the pointer pointing to the resulting array of doubles.

&nbsp;

### Parameter 15: Circuit.AllNodeVMagPUByPhase

This parameter returns a pointer to an array of doubles representing the voltage magnitudes (in per unit) for nodes on the specified phase. The argument Pointer must specify the pointer to the integer containing the phase number when called, the Pointer argument will update when returning results with the pointer pointing to the resulting array of doubles.

&nbsp;

### Parameter 16: Circuit.AllNodeDistancesByPhase

This parameter returns a pointer to an array of doubles representing the distances to parent EnergyMeter. Sequence of array corresponds to other node ByPhase properties. The argument Pointer must specify the pointer to the integer containing the phase number when called, the Pointer argument will update when returning results with the pointer pointing to the resulting array of doubles.

&nbsp;

### Parameter 17: Circuit.AllNodeNamesByPhase

This parameter returns a pointer to an array of strings of the node names by Phase criteria. Sequence corresponds to other ByPhase properties. The argument Pointer must specify the pointer to the integer containing the phase number when called, the Pointer argument will update when returning results with the pointer pointing to the resulting array of Bytes (string).

&nbsp;

### Parameter 18: Circuit.YNodeVArray

This parameter returns a pointer to an array of complex of actual node voltages in same order as SystemY Matrix. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).

&nbsp;

### Parameter 19: Circuit.YNodeOrder

This parameter returns a pointer to an array of strings containing the names of the nodes in the same order as the Y Matrix.The names of the elements are separated by a NULL (0) character.

&nbsp;

### Parameter 20: Circuit.YCurrents

This parameter returns a pointer to an array of doubles containing complex injection currents for the present solution. It is the "I" vector of I=YV. Each element is a complex structure including real and imaginary parts (double, 16 Bytes per element).


***
_Created with the Standard Edition of HelpNDoc: [Experience the power of a responsive website for your documentation](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
