# ReactorsF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double ReactorsF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Reactors.kV read

Gets the kV rating of the active reactor.

&nbsp;

### Parameter 1: Reactors.kV write

Sets the kV rating of the active reactor.

&nbsp;

### Parameter 2: Reactors.kvar read

Gets the kvar rating of the active reactor.

&nbsp;

### Parameter 3: Reactors.kvar write

Sets the kvar rating of the active reactor.

&nbsp;

### Parameter 4: Reactors.lmH read

Gets the Inductance, mH for the active reactor.

&nbsp;

### Parameter 5: Reactors.lmH write

Sets the Inductance, mH for the active reactor.

&nbsp;

### Parameter 6: Reactors.R read

Gets the Resistance (in series with reactance), each phase, ohms for the active reactor.

&nbsp;

### Parameter 7: Reactors.R write

Sets the Resistance (in series with reactance), each phase, ohms for the active reactor.

&nbsp;

### Parameter 8: Reactors.Rp read

Gets the Resistance in parallel with R and X (the entire branch) for the active reactor.

&nbsp;

### Parameter 9: Reactors.Rp write

Sets the Resistance in parallel with R and X (the entire branch) for the active reactor.

&nbsp;

### Parameter 10: Reactors.X read

Gets the Reactance, each phase, ohms at base frequency for the active reactor.

&nbsp;

### Parameter 11: Reactors.X write

Sets the Reactance, each phase, ohms at base frequency for the active reactor.

***
_Created with the Standard Edition of HelpNDoc: [Step-by-Step Guide: How to Turn Your Word Document into an eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
