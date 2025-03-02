# CircuitI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t CircuitI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer according to the number sent in the variable “parameter”. The parameter can be one of the following:

&nbsp;

### Parameter 0: Circuit.NumCktElements

This parameter will deliver the number of CktElements included in the active circuit.

&nbsp;

### Parameter 1: Circuit.NumBuses

This parameter will deliver the number of buses included in the active circuit.

&nbsp;

### Parameter 2: Circuit.NumNodes

This parameter will deliver the number of nodes included in the active circuit.

&nbsp;

### Parameter 3: Circuit.FirstPCElement

This parameter sets the first PCElement to be the active PCElement, as a result, this parameter will deliver the index of the active PCElement (ideally 1).

&nbsp;

### Parameter 4: Circuit.NextPCElement

This parameter sets the next PCElement to be the active PCElement, as a result, this parameter will deliver the index of the active PCElement (if there is no more it will return a 0).

&nbsp;

### Parameter 5: Circuit.FirstPDElement

This parameter sets the first PDElement to be the active PDElement, as a result, this parameter will deliver the index of the active PDElement (ideally 1).

&nbsp;

### Parameter 6: Circuit.NextPDElement

This parameter sets the next PDElement to be the active PDElement, as a result, this parameter will deliver the index of the active PDElement (if there is no more it will return a 0).

&nbsp;

### Parameter 7: Circuit.Sample

This parameter forces all meters and monitors to take a sample, returns 0.

&nbsp;

### Parameter 8: Circuit.SaveSample

This parameter forces all meters and monitors to save their sample buffers, returns 0.

&nbsp;

### Parameter 9: Circuit.SetActiveBusi

This parameter sets active the bus specified by index, which is compatible with the index delivered by AllBusNames, returns 0 it everything ok.

&nbsp;

### Parameter 10: Circuit.FirstElement

This parameter sets the first Element of the active class to be the active Element, as a result, this parameter will deliver the index of the active Element (0 if none).

&nbsp;

### Parameter 11: Circuit.NextElement

This parameter sets the next Element of the active class to be the active Element, as a result, this parameter will deliver the index of the active Element (0 if none).

&nbsp;

### Parameter 12: Circuit.UpdateStorage

This parameter forces all storage classes to update. Typically done after a solution.

&nbsp;

### Parameter 13: Circuit.ParentPDElement

This parameter sets parent PD Element, if any, to be the active circuit element and returns index \> 0 if it fails or not applicable.

&nbsp;

### Parameter 14: Circuit.EndofTimeStepUpdate

This parameter calls end of time step cleanup routine in solutionalgs.pas. Returns 0.


***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Ease of Use of HelpNDoc for CHM Help File Generation](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
