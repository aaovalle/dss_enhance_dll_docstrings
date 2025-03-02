# StoragesI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t StoragesI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Storages.First

Set first Storage element active; returns 0 if none.

&nbsp;

### Parameter 1: Storages.Next

Sets next Storage element active; returns 0 if no more.

&nbsp;

### Parameter 2: Storages.Count

Returns the number of Storage Elements.

&nbsp;

### Parameter 3: Storages.Idx read

This parameter gets the active Storage element by index:&nbsp; 1.. Count

&nbsp;

### Parameter 4: Storages.Idx write

This parameter sets the active Storage element by index:&nbsp; 1.. Count.

&nbsp;

### Parameter 5: Storages.State read

This parameter gets the state of the active storage object: 0=Idling; 1=Discharging; -1=Charging;

&nbsp;

### Parameter 6: Storages.State write

This parameter sets the state of the active storage object: 0=Idling; 1=Discharging; -1=Charging;

&nbsp;

### Parameter 7: Storages.ControloMode read

This parameter gets the control mode for the inverter of the active Storage object. It can be one of {GFM = 1\| GFL\* = 0}.

&nbsp;

### Parameter 8: Storages.ControlMode write

This parameter sets the control mode for the inverter of the active Storage object. It can be one of {GFM = 1\| GFL\* = 0}.

&nbsp;

### Parameter 9: Storages.SafeMode

(Read only) Indicates whether the inverter entered (1) or not (0) into Safe Mode.

&nbsp;

### Parameter 10: Storages.VarFollowInverter read

This parameter gets the Boolean variable (1\|0). Defaults to False (0), which indicates that the reactive power generation/absorption does not respect the inverter status.

&nbsp;

### Parameter 11: Storages.VarFollowInverter write

This parameter sets the Boolean variable (1\|0) indicating that the reactive power generation/absorption does not respect the inverter status.

***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Documentation with HelpNDoc's Project Analyzer Features](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
