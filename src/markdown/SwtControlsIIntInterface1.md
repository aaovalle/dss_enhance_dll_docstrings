# SwtControlsI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t SwtControlsI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: SwtControls.First

This parameter sets the first SwtControl active. Returns 0 if no more.

&nbsp;

### Parameter 1: SwtControls.Next

This parameter sets the next SwtControl active. Returns 0 if no more.

&nbsp;

### Parameter 2: SwtControls.Action read

This parameter gets the open (1) or close (2) action of the switch. No effect if switch is locked. However, reset removes any lock and then closes the switch (shelf state). 0 = none action.

&nbsp;

### Parameter 3: SwtControls.Action write

This parameter sets open (1) or close (2) the switch. No effect if switch is locked. However, reset removes any lock and then closes the switch (shelf state). 0 = none action (see manual for details).

&nbsp;

### Parameter 4: SwtControls.IsLocked read

This parameter gets the lock state: {1 locked \| 0 not locked}.

&nbsp;

### Parameter 5: SwtControls.IsLocked write

This parameter sets the lock to prevent both manual and automatic switch operation.

&nbsp;

### Parameter 6: SwtControls.SwitchedTerm read

This parameter gets the terminal number where the switch is located on the SwitchedObj.

&nbsp;

### Parameter 7: SwtControls.SwitchedTerm write

This parameter sets the terminal number where the switch is located on the SwitchedObj.

&nbsp;

### Parameter 8: SwtControls.Count

This parameter gets the total number of SwtControls in the active circuit.


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Review with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
