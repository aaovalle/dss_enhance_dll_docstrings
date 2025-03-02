# PVSystemsF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double PVSystemsF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: PVSystems.Irradiance read

This parameter gets the present value of the Irradiance property in W/sq-m.

&nbsp;

### Parameter 1: PVSystems.Irradiance write

This parameter sets the present value of the Irradiance property in W/sq-m.

&nbsp;

### Parameter 2: PVSystems.kW

This parameter gets the kW output.

&nbsp;

### Parameter 3: PVSystems.kvar read

This parameter gets the kvar value.

&nbsp;

### Parameter 4: PVSystems.kvar write

This parameter sets the kvar value.

&nbsp;

### Parameter 5: PVSystems.pf read

This parameter gets the power factor value.

&nbsp;

### Parameter 6: PVSystems.pf write

This parameter sets the power factor value.

&nbsp;

### Parameter 7: PVSystems.KVARated read

This parameter gets the rated kVA of the PVSystem.

&nbsp;

### Parameter 8: PVSystems.KVARated write

This parameter sets the rated kVA of the PVSystem.

&nbsp;

### Parameter 9: PVSystems.pmpp read

This parameter gets the rated max power of the PV array for 1.0 kW/sq-m irradiance and a user-selected array temperature of the active PVSystem.

&nbsp;

### Parameter 10: PVSystems.pmpp write

This parameter sets the rated max power of the PV array for 1.0 kW/sq-m irradiance and a user-selected array temperature of the active PVSystem.

&nbsp;

### Parameter 11: PVSystems.IrradianceNow

This parameter returns the current irradiance value of the active PVSystem. The current irradiance value is the one provided by the irradiance shape linked to the PV, use it to get this information while running simulations.


***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with HelpNDoc's Intuitive Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
