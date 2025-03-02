# IsourcesF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double IsourcesF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Isources.Amps read

This parameter gets the magnitude of the Isource in Amps.

&nbsp;

### Parameter 1: Isources.Amps write

This parameter sets the magnitude of the Isource in Amps.

&nbsp;

### Parameter 2: Isources.AngleDeg read

This parameter gets the phase angle of the Isource in degrees.

&nbsp;

### Parameter 3: Isources.AngleDeg write

This parameter sets the phase angle of the Isource in degrees.

&nbsp;

### Parameter 4: Isources.Frequency read

This parameter gets the frequency of the Isource in Hz.

&nbsp;

### Parameter 5: Isources.Frequency write

This parameter sets the frequency of the Isource in Hz.


***
_Created with the Standard Edition of HelpNDoc: [Achieve Professional Documentation Results with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
