# GeneratorsF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double GeneratorsF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Generators.kV read

This parameter gets the voltage base for the active generator, kV.

&nbsp;

### Parameter 1: Generators.kV Write

This parameter sets the voltage base for the active generator, kV.

&nbsp;

### Parameter 2: Generators.kW read

This parameter gets the kW output for the active generator, kvar is updated for current power factor.

&nbsp;

### Parameter 3: Generators.kW Write

This parameter sets the kW output for the active generator, kvar is updated for current power factor.

&nbsp;

### Parameter 4: Generators.kvar read

This parameter gets the kvar output for the active generator, kW is updated for current power factor.

&nbsp;

### Parameter 5: Generators.kvar Write

This parameter sets the kvar output for the active generator, kW is updated for current power factor.

&nbsp;

### Parameter 6: Generators.Pf read

This parameter gets the power factor (pos. = producing vars). Updates kvar based on present kW value.

&nbsp;

### Parameter 7: Generators.Pf Write

This parameter sets the power factor (pos. = producing vars). Updates kvar based on present kW value.

&nbsp;

### Parameter 8: Generators.KVARated read

This parameter gets the KVA rating of the generator.

&nbsp;

### Parameter 9: Generators.KVARated Write

This parameter sets the KVA rating of the generator.

&nbsp;

### Parameter 10: Generators.Vmaxpu read

This parameter gets the Vmaxpu for Generator Model.

&nbsp;

### Parameter 11: Generators.VMaxpu Write

This parameter sets the Vmaxpu for Generator Model.

&nbsp;

### Parameter 12: Generators.Vminpu read

This parameter gets the Vminpu for Generator Model.

&nbsp;

### Parameter 13: Generators.VMinpu Write

This parameter sets the Vminpu for Generator Model.


***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Help Documentation with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
