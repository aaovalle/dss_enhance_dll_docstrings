# BusF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double BUSF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number (64 bits) according to the number sent in the variable “parameter”. The parameter can be one of the following:

&nbsp;

### Parameter 0: Bus.kVBase

This parameter returns the base voltage at bus in kV.

&nbsp;

### Parameter 1: Bus.X - read

This parameter returns the X coordinate for the bus.

&nbsp;

### Parameter 2: Bus.X - Write

This parameter allows to write the X coordinate for the bus. Returns 0.

&nbsp;

### Parameter 3: Bus.Y - read

This parameter returns the Y coordinate for the bus.

&nbsp;

### Parameter 4: Bus.Y - Write

This parameter allows to write the Y coordinate for the bus. Returns 0.

&nbsp;

### Parameter 5: Bus.Distance

This parameter returns the distance from the energymeter (if non-zero).

&nbsp;

### Parameter 6: Bus.Lambda

This parameter returns the accumulated failure rate downstream from this bus; faults per year.

&nbsp;

### Parameter 7: Bus.N\_Interrupts

This parameter returns the number of interruptions this bus per year.

&nbsp;

### Parameter 8: Bus.Int\_Duration

This parameter returns the average interruption duration in hours.

&nbsp;

### Parameter 9: Bus.Cust\_interrupts

This parameter returns the annual number of customer interruptions from this bus.

&nbsp;

### Parameter 10: Bus.Cust\_duration

This parameter returns the accumulated customer outage duration.

&nbsp;

### Parameter 11: Bus.Totalmiles

This parameter returns the total length of line down line from this bus, in miles. For recloser siting algorithm.

&nbsp;

### Parameter 12: Bus.Latitude read

This parameter returns the GIS latitude assigned to the active bus (if any).

&nbsp;

### Parameter 13: Bus.Latitude Write

This parameter sets the GIS latitude to the active bus using the value given at the argument.

&nbsp;

### Parameter 14: Bus.Longitude read

This parameter returns the GIS longitude assigned to the active bus (if any).

&nbsp;

### Parameter 15: Bus.Longitude Write

This parameter sets the GIS longitude to the active bus using the value given at the argument.


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your PDF Protection with These Simple Steps](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
