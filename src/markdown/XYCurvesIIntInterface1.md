# XYCurvesI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t XYCurvesI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: XYCurves.Count

This parameter gets number of XYCurves in active circuit.

&nbsp;

### Parameter 1: XYCurves.First

This parameter sets first XYCurves object active; returns 0 if none.

&nbsp;

### Parameter 2: XYCurves.Next

This parameter sets next XYCurves object active; returns 0 if none.

&nbsp;

### Parameter 3: XYCurves.Npts read

This parameter gets the number of points in X-Y curve.

&nbsp;

### Parameter 4: XYCurves.Npts read

This parameter sets the number of points in X-Y curve.


***
_Created with the Standard Edition of HelpNDoc: [Say Goodbye to Documentation Headaches with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
