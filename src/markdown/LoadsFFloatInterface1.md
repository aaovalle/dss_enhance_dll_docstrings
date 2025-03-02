# Loads F (Float) Interface

&nbsp;

This interface can be used to read/modify the properties of the Loads Class where the values are floating point numbers (double). The structure of the interface is as follows:

&nbsp;

double DSSLoadsF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a Double (IEEE 754 64 bits), the variable “parameter” (Integer) is used to specify the property of the class to be used and the variable “argument” (double) can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: Loads.kw – Read

This parameter allows to read the kW property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 1: Load.kw – Write

This parameter allows to write the kW property of the active load. The parameter argument must contain the new value in kW for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 2: Loads.kV – Read

This parameter allows to read the kV property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 3: Load.kV – Write

This parameter allows to write the kV property of the active load. The parameter argument must contain the new value in kV for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 4: Loads.kvar – Read

This parameter allows to read the kvar property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 5: Load.kvar – Write

This parameter allows to write the kvar property of the active load. The parameter argument must contain the new value in kvar for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 6: Loads.pf – Read

This parameter allows to read the pf property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 7: Load.pf – Write

This parameter allows to write the pf property of the active load. The parameter argument must contain the new value in pf for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 8: Loads.PctMean – Read

This parameter allows to read the PctMean property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 9: Load.PctMean – Write

This parameter allows to write the PctMean property of the active load. The parameter argument must contain the new value in PctMean for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 10: Loads.PctStdDev – Read

This parameter allows to read the PctStdDev property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 11: Load.PctStdDev – Write

This parameter allows to write the PctStdDev property of the active load. The parameter argument must contain the new value in PctStdDev for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 12: Loads.AllocationFactor – Read

This parameter allows to read the AllocationFactor property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 13: Load. AllocationFactor – Write

This parameter allows to write the AllocationFactor property of the active load. The parameter argument must contain the new value in AllocationFactor for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 14: Loads.CFactor – Read

This parameter allows to read the CFactor property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 15: Load. CFactor – Write

This parameter allows to write the CFactor property of the active load. The parameter argument must contain the new value in CFactor for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 16: Loads.CVRWatts – Read

This parameter allows to read the CVRWatts property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 17: Load.CVRWatts – Write

This parameter allows to write the CVRWatts property of the active load. The parameter argument must contain the new value in CVRWatts for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 18: Loads.CVRvars – Read

This parameter allows to read the CVRvars property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 19: Load.CVRvars – Write

This parameter allows to write the CVRvars property of the active load. The parameter argument must contain the new value in CVRvars for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 20: Loads.kva – Read

This parameter allows to read the kva property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 21: Load.kva – Write

This parameter allows to write the kva property of the active load. The parameter argument must contain the new value in kva for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 22: Loads.kWh – Read

This parameter allows to read the kWh property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 23: Load.kWh – Write

This parameter allows to write the kWh property of the active load. The parameter argument must contain the new value in kWh for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 24: Loads.kWhdays – Read

This parameter allows to read the kWhdays property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 25: Load.kWhdays – Write

This parameter allows to write the kWhdays property of the active load. The parameter argument must contain the new value in kWhdays for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 26: Loads.RNeut – Read

This parameter allows to read the RNeut (neutral resistance for wye connected loads) property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 27: Load.RNeut – Write

This parameter allows to write the RNeut (neutral resistance for wye connected loads) property of the active load. The parameter argument must contain the new value in RNeut for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 28: Loads.VMaxpu – Read

This parameter allows to read the VMaxpu property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 29: Load.VMaxpu – Write

This parameter allows to write the VMaxpu property of the active load. The parameter argument must contain the new value in VMaxpu for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 30: Loads.VMinemerg – Read

This parameter allows to read the VMinemerg property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 31: Load.VMinemerg – Write

This parameter allows to write the VMinemerg property of the active load. The parameter argument must contain the new value in VMinemerg for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 32: Loads.VMinnorm – Read

This parameter allows to read the VMinnorm property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 33: Load.VMinnorm – Write

This parameter allows to write the VMinnorm property of the active load. The parameter argument must contain the new value in VMinnorm for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 34: Loads.VMinpu – Read

This parameter allows to read the VMinpu property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 35: Load.VMinpu – Write

This parameter allows to write the VMinpu property of the active load. The parameter argument must contain the new value in VMinpu for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 36: Loads.xfKVA – Read

This parameter allows to read the xfKVA (Rated service transformer KVA for load allocation, using Allocationfactor. Affects kW, kvar and pf.) property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 37: Load.xfKVA – Write

This parameter allows to write the xfKVA (Rated service transformer KVA for load allocation, using Allocationfactor. Affects kW, kvar and pf.) property of the active load. The parameter argument must contain the new value in xfKVA for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 38: Loads.Xneut – Read

This parameter allows to read the Xneut property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 39: Load. Xneut – Write

This parameter allows to write the Xneut property of the active load. The parameter argument must contain the new value in Xneut for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 40: Loads.PctSeriesRL – Read

This parameter allows to read the PctSeriesRL (Percent of Load that is modeled as series R-L for harmonic studies) property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 41: Load.PctSeriesRL – Write

This parameter allows to write the PctSeriesRL (Percent of Load that is modeled as series R-L for harmonic studies) property of the active load. The parameter argument must contain the new value in PctSeriesRL for the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 42: Loads.RelWeight – Read

This parameter allows to read the RelWeight (relative weighting factor) property of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 43: Loads.RelWeight – Write

This parameter allows to write the RelWeight (relative weighting factor) property of the active load. The parameter argument must contain the new value in RelWeight for the desired active load. The return value will be equal to 0.


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Publish Your Word Document as an eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
