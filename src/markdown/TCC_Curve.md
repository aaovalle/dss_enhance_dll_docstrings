# TCC_Curve

&nbsp;

A TCC\_Curve object is defined similarly to Loadshape and Growthshape objects in that they all are defined by curves consisting of arrays of points. Intended to model time-current characteristics for overcurrent relays, TCC\_Curve objects are also used for other relay types requiring time curves. Both the time array and the C array must be entered.

&nbsp;

The properties are:

&nbsp;

Npts= Number of points to expect when defining the curve.

C\_Array= Array of current (or voltage or whatever) values corresponding to time values in T\_Array (see T\_Array).

T\_Array= Array of time values in sec. Typical array syntax:

t\_array = (1, 2, 3, 4, ...) You may also substitute a file designation: t\_array = (file=filename). The specified file has one value per line.

Like= Name of an existing GrowthShape object to base this one on.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Single source CHM, PDF, DOC and HTML Help creation](<https://www.helpndoc.com/help-authoring-tool>)_
