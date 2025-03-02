# CapControlsF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double CapControlsF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number (64 bits) with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: CapControls.CTRatio read

This parameter gets the transducer ratio current to control current.

&nbsp;

### Parameter 1: CapControls.CTRatio write

This parameter sets the transducer ratio current to control current.

&nbsp;

### Parameter 2: CapControls.PTRatio read

This parameter gets the transducer ratio from primary feeder to control voltage.

&nbsp;

### Parameter 3: CapControls.PTRatio write

This parameter sets the transducer ratio from primary feeder to control voltage.

&nbsp;

### Parameter 4: CapControls.ONSetting read

This parameter gets the threshold to arm or switch on a step. See Mode for Units.

&nbsp;

### Parameter 5: CapControls.ONSetting write

This parameter sets the threshold to arm or switch on a step. See Mode for Units.

&nbsp;

### Parameter 6: CapControls.OFFSetting read

This parameter gets the threshold to switch off a step. See Mode for Units.

&nbsp;

### Parameter 7: CapControls.OFFSetting write

This parameter sets the threshold to switch off a step. See Mode for Units.

&nbsp;

### Parameter 8: CapControls.VMax read

This parameter gets the Vmax, this reference with VoltOverride, switch off whenever PT voltage exceeds this level.

&nbsp;

### Parameter 9: CapControls.VMax write

This parameter sets the Vmax, this reference with VoltOverride, switch off whenever PT voltage exceeds this level.

&nbsp;

### Parameter 10: CapControls.VMin read

This parameter gets the Vmin, this reference with VoltOverride, switch ON whenever PT voltage drops below this level.

&nbsp;

### Parameter 11: CapControls.VMin write

This parameter sets the Vmin, this reference with VoltOverride, switch ON whenever PT voltage drops below this level.

&nbsp;

### Parameter 12: CapControls.Delay read

This parameter gets the time delay \[s\] to switch on after arming. Control may reset before actually switching.

&nbsp;

### Parameter 13: CapControls.Delay write

This parameter sets the time delay \[s\] to switch on after arming. Control may reset before actually switching.

&nbsp;

### Parameter 14: CapControls.DelayOff read

This parameter gets the time delay \[s\] before switching off a step. Control may reset before actually switching.

&nbsp;

### Parameter 15: CapControls.DelayOff write

This parameter sets the time delay \[s\] before switching off a step. Control may reset before actually switching.

&nbsp;

### Parameter 16: CapControls.DeadTime read

This parameter gets the time delay \[s\] after switching off a step. Control may reset before actually switching.

&nbsp;

### Parameter 17: CapControls.DeadTime write

This parameter sets the time delay \[s\] after switching off a step. Control may reset before actually switching.


***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
