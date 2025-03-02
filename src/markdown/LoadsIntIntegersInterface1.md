# Loads Int (Integers) Interface

&nbsp;

This interface can be used to read/modify the properties of the Loads Class where the values are integers. The structure of the interface is as follows:

&nbsp;

int32\_t DSSLoads(int32\_t Parameter, int32\_t argument)

&nbsp;

This interface returns an integer (signed 32 bits), the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: Loads.First

This parameter allows to set the active load into the first load registered in the active circuit. As a result, this property will return the number 1. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 1: Loads.Next

This parameter sets the active load into the next load registered in the active circuit. As a result, this property will deliver the index of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 2: Loads.Idx – Read

This parameter allows to read the index of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 3: Load.Idx – Write

This parameter allows to write the index of the active load. The parameter argument must contain the index of the desired active load. The return value will be equal to 0.

&nbsp;

### Parameter 4: Load.Count

This parameter returns the number of load elements within the active circuit. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 5: Load.Class – Read

This parameter allows to read the code number used to separate loads by class or group. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 6: Load.Class – Write

This parameter allows to read the code number used to separate loads by class or group. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 7: Load.Model – Read

This parameter allows to read the model of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 8: Load.Model – Write

This parameter allows to write the model of the active load using the parameter argument. This parameter will return a 0.

&nbsp;

### Parameter 9: Load.NumCust – Read

This parameter allows to read the number of customer of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 10: Load.NumCust – Write

This parameter allows to write the number of customers of the active load using the parameter argument. This parameter will return a 0.

&nbsp;

### Parameter 11: Load.Status – Read

This parameter allows to read Response to load multipliers: Fixed (growth only –“1”), Exempt (no LD curve - “2”), Variable (all – “0”), of the active load. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 12: Load.Status – Write

This parameter allows to write the response to load multipliers: Fixed (growth only – “1”), Exempt (no LD curve – “2”), Variable (all – “0”), of the active load using the parameter argument. This parameter will return a 0.

&nbsp;

### Parameter 13: Load.IsDelta – Read

This parameter allows to read if the active load is connected in delta, if the answer is positive, this function will deliver a 1; otherwise, the answer will be 0. The parameter argument can be filled with a 0.

&nbsp;

### Parameter 14: Load.IsDelta – Write

This parameter allows to write if the active load is connected in delta, if it is, the argument variable must contain a 1; otherwise, 0. The parameter argument can be filled with a 0. This parameter will return a 0.


***
_Created with the Standard Edition of HelpNDoc: [Make your documentation accessible on any device with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
