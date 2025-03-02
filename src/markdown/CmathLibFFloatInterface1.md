# CmathLibF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double CmathLibF(int32\_t Parameter, double Argument1, double Argument2);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: CmathLib.Cabs

This parameter returns the absolute value of complex number given in real (Argument1) and imaginary (Argument2) doubles.

&nbsp;

### Parameter 1: CmathLib.Cdang

This parameter returns the angle, in degrees, of a complex number specified as two doubles: Real part (Argument1) and imaginary part (Argument2).


***
_Created with the Standard Edition of HelpNDoc: [News and information about help authoring tools and software](<https://www.helpauthoringsoftware.com>)_
