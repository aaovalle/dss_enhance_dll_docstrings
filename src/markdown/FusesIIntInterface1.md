# FusesI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t FusesI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Fuses.Count

This parameter returns the number of Fuses objects currently defined in the active circuit.

&nbsp;

### Parameter 1: Fuses.First

This parameter sets the first Fuse to be the active Fuse. Returns 0 if none.

&nbsp;

### Parameter 2: Fuses.Next

This parameter sets the next Fuse to be the active Fuse. Returns 0 if none.

&nbsp;

### Parameter 3: Fuses.MonitoredTerm read

This parameter gets the terminal number to switch the fuse is connected.

&nbsp;

### Parameter 4: Fuses.MonitoredTerm write

This parameter sets the terminal number to switch the fuse is connected.

&nbsp;

### Parameter 5: Fuses.SwitchedTerm read

This parameter gets the terminal number of the terminal containing the switch controlled by the fuse.

&nbsp;

### Parameter 6: Fuses.SwitchedTerm write

This parameter sets the terminal number of the terminal containing the switch controlled by the fuse.

&nbsp;

### Parameter 7: Fuses.Open

Manual opening of fuse.

&nbsp;

### Parameter 8: Fuses.Close

Manual closing of fuse.

&nbsp;

### Parameter 9: Fuses.IsBlown

This parameter returns the current state of the fuses. TRUE (1) if any on any phase is blown. Else FALSE (0)

.

### Parameter 10: Fuses.Idx read

This parameter gets the active fuse by index into the list of fuses. 1 based: 1..count.

&nbsp;

### Parameter 11: Fuses.Idx write

This parameter sets the active fuse by index into the list of fuses. 1 based: 1..count.

&nbsp;

### Parameter 12: Fuses.NumPhases

This parameter gets the number of phases of the active fuse.

&nbsp;

### Parameter 13: Fuses.Reset

This parameter resets the active fuse to its normal state.


***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Help Documentation with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
