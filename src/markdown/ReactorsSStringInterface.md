# ReactorsS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr ReactorsS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Reactors.Name read

Gets the name of the active reactor.

&nbsp;

### Parameter 1: Reactors.Name write

Sets the name of the active reactor.

&nbsp;

### Parameter 2: Reactors.LCurve read

Gets the name of XYCurve object describing per-unit variation of phase inductance, L=X/w, vs. frequency for the active reactor.

&nbsp;

### Parameter 3: Reactors.LCurve write

Sets the name of XYCurve object describing per-unit variation of phase inductance, L=X/w, vs. frequency for the active reactor.

&nbsp;

### Parameter 4: Reactors.RCurve read

Gets the Name of XYCurve object, previously defined, describing per-unit variation of phase resistance, R, vs. frequency for the active reactor.

&nbsp;

### Parameter 5: Reactors.RCurve write

Sets the Name of XYCurve object, previously defined, describing per-unit variation of phase resistance, R, vs. frequency for the active reactor

***
_Created with the Standard Edition of HelpNDoc: [Create cross-platform Qt Help files](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
