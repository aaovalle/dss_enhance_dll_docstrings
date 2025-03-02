# VSourcesF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double VSourcesF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: VSources.BasekV read

This parameter gets the source voltage in kV.

&nbsp;

### Parameter 1: VSources.BasekV write

This parameter sets the source voltage in kV.

&nbsp;

### Parameter 2: VSources.pu read

This parameter gets the source voltage in pu.

&nbsp;

### Parameter 3: VSources.pu write

This parameter sets the source voltage in pu.

&nbsp;

### Parameter 4: VSources.Angledeg read

This parameter gets the source phase angle of first phase in degrees.

&nbsp;

### Parameter 5: VSources.Angledeg write

This parameter sets the source phase angle of first phase in degrees.

&nbsp;

### Parameter 6: VSources.Frequency read

This parameter gets the source frequency in Hz.

&nbsp;

### Parameter 7: VSources.Frequency write

This parameter sets the source frequency in Hz.


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Output with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
