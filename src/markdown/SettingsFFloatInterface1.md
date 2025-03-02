# SettingsF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double SettingsF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Settings.AllocationFactors

This parameter sets all load allocation factors for all loads defined by XFKVA property to this value.

&nbsp;

### Parameter 1: Settings.NormVminpu read

This parameter gets the per unit minimum voltage for Normal conditions.

&nbsp;

### Parameter 2: Settings.NormVminpu write

This parameter sets the per unit minimum voltage for Normal conditions.

&nbsp;

### Parameter 3: Settings.NormVmaxpu read

This parameter gets the per unit maximum voltage for Normal conditions.

&nbsp;

### Parameter 4: Settings.NormVmaxpu write

This parameter sets the per unit maximum voltage for Normal conditions.

&nbsp;

### Parameter 5: Settings.EmergVminpu read

This parameter gets the per unit minimum voltage for Emergency conditions.

&nbsp;

### Parameter 6: Settings.EmergVminpu write

This parameter set the per unit minimum voltage for Emergency conditions.

&nbsp;

### Parameter 7: Settings.EmergVmaxpu read

This parameter gets the per unit maximum voltage for Emergency conditions.

&nbsp;

### Parameter 8: Settings.EmergVmaxpu write

This parameter sets the per unit maximum voltage for Emergency conditions.

&nbsp;

### Parameter 9: Settings.UEWeight read

This parameter gets the weighting factor applied to UE register values.

&nbsp;

### Parameter 10: Settings.UEWeight write

This parameter sets the weighting factor applied to UE register values.

&nbsp;

### Parameter 11: Settings.LossWeight read

This parameter gets the weighting factor applied to Loss register values.

&nbsp;

### Parameter 12: Settings.LossWeight write

This parameter sets the weighting factor applied to Loss register values.

&nbsp;

### Parameter 13: Settings.PriceSignal read

This parameter gets the price signal for the circuit.

&nbsp;

### Parameter 14: Settings.PriceSignal write

This parameter sets the price signal for the circuit.


***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
