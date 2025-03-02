# WindGensF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double WindGensF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: WindGens.Ag read

This parameter gets the Gearbox ratio (Default 1/90).

&nbsp;

### Parameter 1: WindGens.Ag write

This parameter sets the Gearbox ratio (Default 1/90).

&nbsp;

### Parameter 2: WindGens.Cp read

This parameter gets the Turbine performance coefficient (default 0.41).

&nbsp;

### Parameter 3: WindGens.Cp write

This parameter sets the Turbine performance coefficient (default 0.41).

&nbsp;

### Parameter 4: WindGens.kV read

This parameter gets the nominal rated (1.0 per unit) voltage, kV, for WindGen.

&nbsp;

### Parameter 5: WindGens.kV write

This parameter sets the nominal rated (1.0 per unit) voltage, kV, for WindGen.

&nbsp;

### Parameter 6: WindGens.kVA read

This parameter gets the kVA rating of electrical machine. Defaults to 1.2\* kW if not specified.

&nbsp;

### Parameter 7: WindGens.kVA write

This parameter sets the kVA rating of electrical machine. Defaults to 1.2\* kW if not specified.

&nbsp;

### Parameter 8: WindGens.kvar read

This parameter gets the base kvar.&nbsp; Alternative to specifying the power factor.

&nbsp;

### Parameter 9: WindGens.kvar write

This parameter sets the base kvar.&nbsp; Alternative to specifying the power factor.

&nbsp;

### Parameter 10: WindGens.kW read

This parameter gets the total base kW for the WindGen.

&nbsp;

### Parameter 11: WindGens.kW write

This parameter sets the total base kW for the WindGen.

&nbsp;

### Parameter 12: WindGens.Lamda read

This parameter gets the Tip speed ratio (Default 7.95).

&nbsp;

### Parameter 13: WindGens.Lamda write

This parameter sets the Tip speed ratio (Default 7.95).

&nbsp;

### Parameter 14: WindGens.pd read

This parameter gets the air density in kg/m3 (Default 1.225).

&nbsp;

### Parameter 15: WindGens.pd write

This parameter sets the air density in kg/m3 (Default 1.225).

&nbsp;

### Parameter 16: WindGens.PF read

This parameter gets the WindGen power factor. Default is 0.80.

&nbsp;

### Parameter 17: WindGens.PF write

This parameter sets the WindGen power factor. Default is 0.80.

&nbsp;

### Parameter 18: WindGens.Pss read

This parameter gets the Steady state output real power of the active WindGen object.

&nbsp;

### Parameter 19: WindGens.Pss write

This parameter sets the Steady state output real power of the active WindGen object.

&nbsp;

### Parameter 20: WindGens.Qss read

This parameter gets the Steady state output reactive power of the active WindGen object.

&nbsp;

### Parameter 21: WindGens.Qss write

This parameter sets the Steady state output reactive power of the active WindGen object.

&nbsp;

### Parameter 22: WindGens.Rad read

This parameter gets the rotor radius in meters (Default 40), of the active WindGen object.

&nbsp;

### Parameter 23: WindGens.Rad write

This parameter sets the rotor radius in meters (Default 40), of the active WindGen object.

&nbsp;

### Parameter 24: WindGens.RThev read

This parameter gets the per unit Thevenin equivalent R, of the active WindGen object.

&nbsp;

### Parameter 25: WindGens.RThev write

This parameter sets the per unit Thevenin equivalent R, of the active WindGen object.

&nbsp;

### Parameter 26: WindGens.VCutOut read

This parameter gets the Cut-out wind speed for the active wind generator (m/s - default 23).

&nbsp;

### Parameter 27: WindGens.VCutOut write

This parameter sets the Cut-out wind speed for the active wind generator (m/s - default 23).

&nbsp;

### Parameter 28: WindGens.VCutIn read

This parameter gets the Cut-in speed for the active wind generator (m/s - default 5).

&nbsp;

### Parameter 29: WindGens.VCutIn write

This parameter sets the Cut-in speed for the active wind generator (m/s - default 5).

&nbsp;

### Parameter 30: WindGens.Vss read

This parameter gets the Steady state voltage magnitude of the active WindGen object.

&nbsp;

### Parameter 31: WindGens.Vss write

This parameter sets the Steady state voltage magnitude of the active WindGen object.

&nbsp;

### Parameter 32: WindGens.WindSpeed read

This parameter gets the Wind speed in m/s of the active WindGen object.

&nbsp;

### Parameter 33: WindGens.WindSpeed write

This parameter sets the Wind speed in m/s of the active WindGen object.

&nbsp;

### Parameter 34: WindGens.XThev read

This parameter gets the per unit Thevenin equivalent X of the active WindGen object.

&nbsp;

### Parameter 35: WindGens.XThev write

This parameter sets the per unit Thevenin equivalent X of the active WindGen object.

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Edit and Export Markdown Documents](<https://www.helpndoc.com/feature-tour/markdown-import-export-using-helpndoc-help-authoring-tool/>)_
