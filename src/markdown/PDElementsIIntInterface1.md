# PDElementsI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t PDElementsI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: PDElements.Count

This parameter gets number of PDElements in active circuit.

&nbsp;

### Parameter 1: PDElements.First

This parameter sets the first enabled PD element to be the active element. Returns 0 if none found.

&nbsp;

### Parameter 2: PDElements.Next

This parameter sets the next enabled PD element to be the active element. Returns 0 if none found.

&nbsp;

### Parameter 3: PDElements.IsShunt

This parameter returns 1 if the PD element should be treated as a shunt element rather than a series element. Applies to capacitor and reactor elements in particular.

&nbsp;

### Parameter 4: PDElements.NumCustomers

This parameter gets the number of customers in this branch.

&nbsp;

### Parameter 5: PDElements.TotalCustomers

This parameter gets the total number of customers from this branch to the end of the zone.

&nbsp;

### Parameter 6: PDElements.ParentPDElement

This parameter gets the parent PD element to be the active circuit element. Returns 0 if no more elements upline.

&nbsp;

### Parameter 7: PDElements.FromTerminal

This parameter gets the number of the terminal of active PD element that is on the "from" side. This is set after the meter zone is determined.

&nbsp;

### Parameter 8: PDElements.SectionID

This parameter gets the integer ID of the feeder section that this PDElement branch is part of.


***
_Created with the Standard Edition of HelpNDoc: [Experience a User-Friendly Interface with HelpNDoc's Documentation Tool](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
