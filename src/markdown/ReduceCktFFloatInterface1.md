# ReduceCktF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double ReduceCktF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: ReduceCkt.Zmag - read

This property gets the value of impedance value associated with the DoShortLines method. Lines with less impedance will be merged out of the circuit, eliminating one or more buses.

&nbsp;

### Parameter 1: ReduceCkt.Zmag - write

This property sets the value of impedance value associated with the DoShortLines method. Lines with less impedance will be merged out of the circuit, eliminating one or more buses.


***
_Created with the Standard Edition of HelpNDoc: [Produce Kindle eBooks easily](<https://www.helpndoc.com/feature-tour/create-ebooks-for-amazon-kindle>)_
