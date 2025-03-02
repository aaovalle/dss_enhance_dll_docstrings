# RegControlsF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double RegControlsF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: RegControls.CTPrimary read

This parameter gets the CT primary ampere rating (secondary is 0.2 amperes).

&nbsp;

### Parameter 1: RegControls.CTPrimary write

This parameter sets the CT primary ampere rating (secondary is 0.2 amperes).

&nbsp;

### Parameter 2: RegControls.PTRatio read

This parameter gets the PT ratio for voltage control settings.

&nbsp;

### Parameter 3: RegControls.PTRatio write

This parameter sets the PT ratio for voltage control settings.

&nbsp;

### Parameter 4: RegControls.ForwardR read

This parameter gets the LDC R settings in Volts.

&nbsp;

### Parameter 5: RegControls.ForwardR write

This parameter sets the LDC R settings in Volts.

&nbsp;

### Parameter 6: RegControls.ForwardX read

This parameter gets the LDC X settings in Volts.

&nbsp;

### Parameter 7: RegControls.ForwardX write

This parameter sets the LDC X settings in Volts.

&nbsp;

### Parameter 8: RegControls.ReverseR read

This parameter gets the reverse LDC R settings in Volts.

&nbsp;

### Parameter 9: RegControls.ReverseR write

This parameter sets the reverse LDC R settings in Volts.

&nbsp;

### Parameter 10: RegControls.ReverseX read

This parameter gets the reverse LDC X settings in Volts.

&nbsp;

### Parameter 11: RegControls.ReverseX write

This parameter sets the reverse LDC X settings in Volts.

&nbsp;

### Parameter 12: RegControls.Delay read

This parameter gets the time delay \[s\] after arming before the first tap change. Control may reset before actually changing taps.

&nbsp;

### Parameter 13: RegControls.Delay write

This parameter sets the time delay \[s\] after arming before the first tap change. Control may reset before actually changing taps.

&nbsp;

### Parameter 14: RegControls.TapDelay read

This parameter gets the time delay \[s\] for subsequent tap changes in a set. Control may reset before actually changing taps.

&nbsp;

### Parameter 15: RegControls.TapDelay write

This parameter sets the time delay \[s\] for subsequent tap changes in a set. Control may reset before actually changing taps.

&nbsp;

### Parameter 16: RegControls.VoltageLimit read

This parameter gets the first house voltage limit on PT secondary base. Setting to 0 disables this function.

&nbsp;

### Parameter 17: RegControls.VoltageLimit write

This parameter sets the first house voltage limit on PT secondary base. Setting to 0 disables this function.

&nbsp;

### Parameter 18: RegControls.ForwardBand read

This parameter gets the regulation bandwidth in forward direction, centered on Vreg.

&nbsp;

### Parameter 19: RegControls.ForwardBand write

This parameter sets the regulation bandwidth in forward direction, centered on Vreg.

&nbsp;

### Parameter 20: RegControls.ForwardVreg read

This parameter gets the target voltage in the forward direction, on PT secondary base.

&nbsp;

### Parameter 21: RegControls.ForwardVreg write

This parameter sets the target voltage in the forward direction, on PT secondary base.

&nbsp;

### Parameter 22: RegControls.ReverseBand read

This parameter gets the bandwidth in reverse direction, centered on reverse Vreg.

&nbsp;

### Parameter 23: RegControls.ReverseBand write

This parameter sets the bandwidth in reverse direction, centered on reverse Vreg.

&nbsp;

### Parameter 24: RegControls.ReverseVreg read

This parameter gets the target voltage in the reverse direction, on PT secondary base.

&nbsp;

### Parameter 25: RegControls.ReverseVreg write

This parameter sets the target voltage in the reverse direction, on PT secondary base.


***
_Created with the Standard Edition of HelpNDoc: [Transform Your Documentation Workflow with HelpNDoc's Intuitive UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
