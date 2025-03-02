# LoadShapeI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t LoadShapeI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: LoadShapes.Count

This parameter returns the number of LoadShape objects currently defined in LoadShape collection.

&nbsp;

### Parameter 1: LoadShapes.First

This parameter sets the first loadshape active and return integer index of the loadshape. Returns 0 if no more.

&nbsp;

### Parameter 2: LoadShapes.Next

This parameter sets the next loadshape active and return integer index of the loadshape. Returns 0 if no more.

&nbsp;

### Parameter 3: LoadShapes.Npts read

This parameter gets the number of points in active LoadShape.

&nbsp;

### Parameter 4: LoadShapes.Npts write

This parameter sets the number of points in active LoadShape.

&nbsp;

### Parameter 5: LoadShapes.Normalize

This parameter normalizes the P and Q curves based on either Pbase, Qbase or simply the peak value of the curve.

&nbsp;

### Parameter 6: LoadShapes.UseActual read

This parameter gets a TRUE/FALSE (1/0) to let Loads know to use the actual value in the curve rather than use the value as a multiplier.

&nbsp;

### Parameter 7: LoadShapes.UseActual write

This parameter sets a TRUE/FALSE (1/0 - Argument) to let Loads know to use the actual value in the curve rather than use the value as a multiplier.


***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
