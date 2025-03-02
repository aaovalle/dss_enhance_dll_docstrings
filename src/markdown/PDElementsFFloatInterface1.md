# PDElementsF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double PDElementsF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: PDElements.FaultRate read

This parameter gets the number of failures per year. For LINE elements: Number of failures per unit length per year.

&nbsp;

### Parameter 1: PDElements.FaultRate write

This parameter sets the number of failures per year. For LINE elements: Number of failures per unit length per year.

&nbsp;

### Parameter 2: PDElements.PctPermanent read

This parameter gets the percent of faults that are permanent (require repair). Otherwise, fault is assumed to be transient/temporary.

&nbsp;

### Parameter 3: PDElements.PctPermanent write

This parameter sets the percent of faults that are permanent (require repair). Otherwise, fault is assumed to be transient/temporary.

&nbsp;

### Parameter 4: PDElements.Lambda

This parameter gets the failure rate for this branch. Faults per year including length of line.

&nbsp;

### Parameter 5: PDElements.AccumulatedL

This parameter gets the accumulated failure rate for this branch on down line.

&nbsp;

### Parameter 6: PDElements.RepairTime

This parameter gets the average time to repair a permanent fault on this branch, hours.

&nbsp;

### Parameter 7: PDElements.TotalMiles

This parameter gets the total miles of line from this element to the end of the zone. For recloser siting algorithm.


***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
