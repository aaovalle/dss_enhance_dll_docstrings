# LoadShapeF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double LoadShapeF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: LoadShapes.HrInterval read

This parameter gets the fixed interval time value, hours.

&nbsp;

### Parameter 1: LoadShapes.HrInterval write

This parameter sets the fixed interval time value, hours.

&nbsp;

### Parameter 2: LoadShapes.MinInterval read

This parameter gets the fixed interval time value, in minutes.

&nbsp;

### Parameter 3: LoadShapes.MinInterval write

This parameter sets the fixed interval time value, in minutes.

&nbsp;

### Parameter 4: LoadShapes.PBase read

This parameter gets the base for normalizing P curve. If left at zero, the peak value is used.

&nbsp;

### Parameter 5: LoadShapes.PBase write

This parameter sets the base for normalizing P curve. If left at zero, the peak value is used.

&nbsp;

### Parameter 6: LoadShapes.QBase read

This parameter gets the base for normalizing Q curve. If left at zero, the peak value is used.

&nbsp;

### Parameter 7: LoadShapes.QBase write

This parameter sets the base for normalizing Q curve. If left at zero, the peak value is used.

&nbsp;

### Parameter 8: LoadShapes.Sinterval read

This parameter gets the fixed interval data time interval, seconds.

&nbsp;

### Parameter 9: LoadShapes.Sinterval write

This parameter sets the fixed interval data time interval, seconds.


***
_Created with the Standard Edition of HelpNDoc: [Easily Add Encryption and Password Protection to Your PDFs](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
