# ReduceCktI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t ReduceCktI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: ReduceCkt.Do1phLaterals

This method removes all 1-phase laterals in the active EnergyMeter’s zone. Loads and other shunt elements are moved to the parent 3-phase bus.

&nbsp;

### Parameter 1: ReduceCkt.DoBranchRemove

This method removes (disable) all branches down-line from the active PDelement. Circuit must have an Energymeter on this branch. If KeepLoad=Y (default) a new Load element is defined and kW, kvar set to present power flow solution for the first element eliminated. The EditString is applied to each new Load element defined.

&nbsp;

### Parameter 2: ReduceCkt.DoDangling

This method reduces Dangling Algorithm; branches with nothing connected.

&nbsp;

### Parameter 3: ReduceCkt.DoDefault

This method Executes the default circuit reduction, which eliminates all dangling end buses and buses without load.

&nbsp;

### Parameter 4:ReduceCkt.DoLoopBreak

This method breaks (disables) all the loops found in the active circuit. Disables one of the Line objects at the head of a loop to force the circuit to be radial.

&nbsp;

### Parameter 5: ReduceCkt.DoParallelLines

This method merges all parallel lines found in the circuit to facilitate its reduction.

&nbsp;

### Parameter 6: ReduceCkt.DoShortLines

This method executes the Do ShortLines algorithm: Set Zmag first if you don't want the default.

&nbsp;

### Parameter 7: ReduceCkt.DoSwitches

This method merges Line objects in which the IsSwitch property is true with the down-line Line object.

&nbsp;

### Parameter 8: ReduceCkt.KeepLoad - read

This property gets a flag indicating to keep (1) the load for Reduction options that remove branches.

&nbsp;

### Parameter 9: ReduceCkt.KeepLoad - write

This property sets the flag for indicating to keep (1) the load for Reduction options that remove branches. Set 1 in the argument if want to keep the load for the reduction, otherwise, set the argument 0.


***
_Created with the Standard Edition of HelpNDoc: [Qt Help documentation made easy](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
