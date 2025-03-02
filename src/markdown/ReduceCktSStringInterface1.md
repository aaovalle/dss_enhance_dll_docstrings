# ReduceCktS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr ReduceCktS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: ReduceCkt.EditString - Read

This property gets the string containing the OpenDSS command appended to the BranchRemove option when a new load is defined to represent the load on the removed branch.

&nbsp;

### Parameter 1: ReduceCkt.EditString - Write

This property sets the string containing the OpenDSS command appended to the BranchRemove option when a new load is defined to represent the load on the removed branch. The EditString must be specified in the argument.

&nbsp;

### Parameter 2: ReduceCkt.EnergyMeter - Read

This property gets the name of EnergyMeter object for circuit reduction.

&nbsp;

### Parameter 3: ReduceCkt.EnergyMeter - Write

This property sets the name of EnergyMeter object for circuit reduction. The name of the EnergyMeter must be specified in the argument.

&nbsp;

### Parameter 4: ReduceCkt.SaveCircuit

This method executes the Save Circuit command from the COM interface. Saves the reduced circuit in a directory with the specified name. The full path name of the Master.DSS file is return in the DSSText.Result property. The name of the circuit must be specified in the argument.

&nbsp;

### Parameter 5: ReduceCkt.StartPDElement - Read

This property gets the full name of the first PDelement for the BranchRemove command (class.name -\> e.g. Line.myLine).

&nbsp;

### Parameter 6: ReduceCkt.StartPDElement - Write

This property sets the full name of the first PDelement for the BranchRemove command (class.name -\> e.g. Line.myLine). The PDElement name must be specified in the argument.


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Efficiency with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
