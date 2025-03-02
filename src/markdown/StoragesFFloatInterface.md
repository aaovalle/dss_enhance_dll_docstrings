# StoragesF (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

double StoragesF(int32\_t Parameter, double Argument);

&nbsp;

This interface returns a floating point number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Storages.puSOC read

This parameter gets the Per unit state of charge of the active Storage object.

&nbsp;

### Parameter 1: Storages.puSOC write

This parameter sets the Per unit state of charge of the active Storage object.

&nbsp;

### Parameter 2: Storages.AmpLimit read

This parameter gets the current limiter per phase for the IBR when operating in GFM mode.

&nbsp;

### Parameter 3: Storages.AmpLimit write

This parameter sets the current limiter per phase for the IBR when operating in GFM mode.

&nbsp;

### Parameter 4: Storages.AmpLimitGain read

This parameter gets the controller gain for fine tuning the current limiter when active, by default is 0.8.&nbsp;

&nbsp;

### Parameter 5: Storages.AmpLimitGain write

This parameter sets the controller gain for fine tuning the current limiter when active, by default is 0.8.&nbsp;

&nbsp;

### Parameter 6: Storages.ChargeTrigger read

This parameter gets the dispatch trigger value for charging the active Storage object.

&nbsp;

### Parameter 7: Storages.ChargeTrigger write

This parameter sets the dispatch trigger value for charging the active Storage object.&nbsp;

&nbsp;

### Parameter 8: Storages.DischargeTrigger read

This parameter gets the dispatch trigger value for discharging the active Storage object.

&nbsp;

### Parameter 9: Storages.DischargeTrigger write

This parameter sets the dispatch trigger value for discharging the active Storage object.&nbsp;

&nbsp;

### Parameter 10: Storages.EffCharge read

This parameter gets the Percentage efficiency for CHARGING the active Storage element. Default = 90.

&nbsp;

### Parameter 11: Storages.EffCharge write

This parameter sets the Percentage efficiency for CHARGING the active Storage element. Default = 90.

&nbsp;

### Parameter 12: Storages.EffDischarge read

This parameter gets the Percentage efficiency for DISCHARGING the active Storage element. Default = 90.

&nbsp;

### Parameter 13: Storages.EffDischarge write

This parameter sets the Percentage efficiency for DISCHARGING the active Storage element. Default = 90.

&nbsp;

### Parameter 14: Storages.kP read

This parameter gets the proportional gain for the PI controller within the inverter of the active Storage object.&nbsp;

&nbsp;

### Parameter 15: Storages.kP write

This parameter sets the proportional gain for the PI controller within the inverter of the active Storage object. Use it to modify the controller response in dynamics simulation mode.

&nbsp;

### Parameter 16: Storages.kV read

This parameter gets the nominal rated (1.0 per unit) voltage, kV, of the active Storage object.&nbsp;

&nbsp;

### Parameter 17: Storages.kV write

This parameter sets the nominal rated (1.0 per unit) voltage, kV, of the active Storage object.&nbsp;

&nbsp;

### Parameter 18: Storages.kVA read

This parameter gets the inverter nameplate capability (in kVA). Used as the base for Dynamics mode and Harmonics mode values.

&nbsp;

### Parameter 19: Storages.kVA write

This parameter sets the inverter nameplate capability (in kVA). Used as the base for Dynamics mode and Harmonics mode values.&nbsp;

&nbsp;

### Parameter 20: Storages.kvar read

This parameter gets the requested kvar value. Final kvar is subjected to the inverter ratings. Sets inverter to operate in constant kvar mode.

&nbsp;

### Parameter 21: Storages.kvar write

This parameter sets the requested kvar value. Final kvar is subjected to the inverter ratings. Sets inverter to operate in constant kvar mode.

&nbsp;

### Parameter 22: Storages.kVDC read

This parameter gets the rated voltage (kV) at the input of the inverter while the storage is discharging.

&nbsp;

### Parameter 23: Storages.kVDC write

This parameter sets the rated voltage (kV) at the input of the inverter while the storage is discharging.

&nbsp;

### Parameter 24: Storages.kW read

This parameter gets the requested kW value. Final kW is subjected to the inverter ratings.

&nbsp;

### Parameter 25: Storages.kW write

This parameter sets the requested kW value. Final kW is subjected to the inverter ratings.

&nbsp;

### Parameter 26: Storages.kWhRated read

This parameter gets the Rated Storage capacity in kWh. Default is 50..

&nbsp;

### Parameter 27: Storages.kWhRated write

This parameter sets the Rated Storage capacity in kWh. Default is 50.

&nbsp;

### Parameter 28: Storages.kWRated read

This parameter gets the kW rating of power output. Base for Loadshapes when DispMode=Follow. Sets kVA property if it has not been specified yet. Defaults to 25.

&nbsp;

### Parameter 29: Storages.kWRated write

This parameter sets the kW rating of power output. Base for Loadshapes when DispMode=Follow. Sets kVA property if it has not been specified yet. Defaults to 25.

&nbsp;

### Parameter 30: Storages.LimitCurrent read

This parameter gets the flag indicating if the Limit current magnitude is active. Limits current magnitude to Vminpu value for both 1-phase and 3-phase Storage similar to Generator Model 7. For 3-phase, limits the positive-sequence current but not the negative-sequence.

&nbsp;

### Parameter 31: Storages.LimitCurrent write

This parameter sets the flag indicating if the Limit current magnitude is active. Limits current magnitude to Vminpu value for both 1-phase and 3-phase Storage similar to Generator Model 7. For 3-phase, limits the positive-sequence current but not the negative-sequence.

&nbsp;

### Parameter 32: Storages.PF read

This parameter gets the requested PF value.&nbsp;

&nbsp;

### Parameter 33: Storages.PF write

This parameter sets the requested PF value.&nbsp;

&nbsp;

### Parameter 34: Storages.PITol read

This parameter gets the tolerance (%) for the closed loop controller of the inverter.

&nbsp;

### Parameter 35: Storages.PITol write

This parameter sets the tolerance (%) for the closed loop controller of the inverter.

&nbsp;

### Parameter 36: Storages.SafeVoltage read

This parameter gets the voltage level (%) respect to the base voltage level for which the Inverter will operate.

&nbsp;

### Parameter 37: Storages.SafeVoltage write

This parameter sets the voltage level (%) respect to the base voltage level for which the Inverter will operate.

&nbsp;

### Parameter 38: Storages.TimeChargeTrig read

This parameter gets the Time of day in fractional hours (0230 = 2.5) at which Storage element will automatically go into charge state. Default is 2.0.&nbsp;

&nbsp;

### Parameter 39: Storages.TimeChargeTrig write

This parameter sets the Time of day in fractional hours (0230 = 2.5) at which Storage element will automatically go into charge state. Default is 2.0.&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Productivity with HelpNDoc's CHM Help File Creation Features](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
