# FusesF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double FusesF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Fuses.RatedCurrent read

This parameter gets the multiplier or actual amps for the TCCcurve object. Defaults to 1.0, Multiply current values of TCC curve by this to get actual amps.

&nbsp;

### Parameter 1: Fuses.RatedCurrent write

This parameter sets the multiplier or actual amps for the TCCcurve object. Defaults to 1.0, Multiply current values of TCC curve by this to get actual amps.

&nbsp;

### Parameter 2: Fuses.Delay read

This parameter gets the fixed delay time in seconds added to the fuse blowing time determined by the TCC curve. Default is 0.

&nbsp;

### Parameter 3: Fuses.Delay write

This parameter sets the fixed delay time in seconds added to the fuse blowing time determined by the TCC curve. Default is 0.


***
_Created with the Standard Edition of HelpNDoc: [Streamline your documentation process with HelpNDoc's HTML5 template](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
