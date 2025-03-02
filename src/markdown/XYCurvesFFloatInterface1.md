# XYCurvesF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double XYCurvesF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: XYCurves.X read

This parameter gets the interpolated value after setting Y.

&nbsp;

### Parameter 1: XYCurves.X write

This parameter sets the X value.

&nbsp;

### Parameter 2: XYCurves.Y read

This parameter gets the interpolated value after setting X.

&nbsp;

### Parameter 3: XYCurves.Y write

This parameter sets the Y value.

&nbsp;

### Parameter 4: XYCurves.XShift read

This parameter gets the amount to shift X value from original curve.

&nbsp;

### Parameter 5: XYCurves.XShift write

This parameter sets the amount to shift X value from original curve.

&nbsp;

### Parameter 6: XYCurves.YShift read

This parameter gets the amount to shift Y value from original curve.

&nbsp;

### Parameter 7: XYCurves.YShift write

This parameter sets the amount to shift Y value from original curve.

&nbsp;

### Parameter 8: XYCurves.XScale read

This parameter gets the factor to scale X values from original curve.

&nbsp;

### Parameter 9: XYCurves.XScale write

This parameter sets the factor to scale X values from original curve.

&nbsp;

### Parameter 10: XYCurves.YScale read

This parameter gets the factor to scale Y values from original curve.

&nbsp;

### Parameter 11: XYCurves.YScale write

This parameter sets the factor to scale Y values from original curve.


***
_Created with the Standard Edition of HelpNDoc: [Add an Extra Layer of Security to Your PDFs with Encryption](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
