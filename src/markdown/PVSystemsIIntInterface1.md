# PVSystemsI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t PVSystemsI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: PVSystems.Count

This parameter returns the number of PVSystem objects currently defined in the active circuit.

&nbsp;

### Parameter 1: PVSystems.First

This parameter sets the first PVSystem to be active; returns 0 if none.

&nbsp;

### Parameter 2: PVSystems.Next

This parameter sets the next PVSystem to be active; returns 0 if none.

&nbsp;

### Parameter 3: PVSystems.Idx read

This parameter gets the active PVSystem by index; 1..Count.

&nbsp;

### Parameter 4: PVSystems.Idx write

This parameter sets the active PVSystem by index; 1..Count.


***
_Created with the Standard Edition of HelpNDoc: [Transform Your Documentation Process with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
