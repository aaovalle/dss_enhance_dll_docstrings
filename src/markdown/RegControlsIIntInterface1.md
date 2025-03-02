# RegControlsI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t RegControlsI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: RegControls.First

This parameter sets the first RegControl active. Returns 0 if no more.

&nbsp;

### Parameter 1: RegControls.Next

This parameter sets the next RegControl active. Returns 0 if no more.

&nbsp;

### Parameter 2: RegControls.TapWinding read

This parameter gets the tapped winding number.

&nbsp;

### Parameter 3: RegControls.TapWinding write

This parameter sets the tapped winding number.

&nbsp;

### Parameter 4: RegControls.Winding read

This parameter gets the winding number for PT and CT connections.

&nbsp;

### Parameter 5: RegControls.Winding write

This parameter sets the winding number for PT and CT connections.

&nbsp;

### Parameter 6: RegControls.IsReversible read

This parameter gets the setting in the reverse direction, usually not applicable to substation transformers.

&nbsp;

### Parameter 7: RegControls.IsReversible read

This parameter sets the different settings for the reverse direction (see Manual for details), usually not applicable to substation transformers.

&nbsp;

### Parameter 8: RegControls.IsInverseTime read

This parameter gets the inverse time feature. Time delay is inversely adjusted, proportional to the amount of voltage outside the regulator band.

&nbsp;

### Parameter 9: RegControls.IsInverseTime write

This parameter sets the inverse time feature. Time delay is inversely adjusted, proportional to the amount of voltage outside the regulator band.

&nbsp;

### Parameter 10: RegControls.MaxTapChange read

This parameter gets the maximum tap change per iteration in STATIC solution mode. 1 is more realistic, 16 is the default for faster solution.

&nbsp;

### Parameter 11: RegControls.MaxTapChange write

This parameter sets the maximum tap change per iteration in STATIC solution mode. 1 is more realistic, 16 is the default for faster solution.

&nbsp;

### Parameter 12: RegControls.Count

This parameter gets the number of RegControl objects in Active Circuit.

&nbsp;

### Parameter 13: RegControls.TapNumber read

This parameter gets the actual tap number of the active RegControl.

&nbsp;

### Parameter 14: RegControls.TapNumber write

This parameter sets the actual tap number of the active RegControl.


***
_Created with the Standard Edition of HelpNDoc: [What is a Help Authoring tool?](<https://www.helpauthoringsoftware.com>)_
