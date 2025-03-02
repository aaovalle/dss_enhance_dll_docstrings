# ReclosersI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t ReclosersI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Reclosers.Count

This parameter gets number of Reclosers in active circuit.

&nbsp;

### Parameter 1: Reclosers.First

This parameter sets first recloser to be active Circuit Element. Returns 0 if none.

&nbsp;

### Parameter 2: Reclosers.Next

This parameter sets next recloser to be active Circuit Element. Returns 0 if none.

&nbsp;

### Parameter 3: Reclosers.MonitoredTerm read

This parameter gets the terminal number of Monitored Object for the Recloser.

&nbsp;

### Parameter 4: Reclosers.MonitoredTerm write

This parameter sets the terminal number of Monitored Object for the Recloser.

&nbsp;

### Parameter 5: Reclosers.SwitchedTerm read

This parameter gets the terminal of the controlled device being switched by the Recloser.

&nbsp;

### Parameter 6: Reclosers.SwitchedTerm write

This parameter sets the terminal of the controlled device being switched by the Recloser.

&nbsp;

### Parameter 7: Reclosers.NumFast read

This parameter gets the number of fast shots.

&nbsp;

### Parameter 8: Reclosers.NumFast write

This parameter sets the number of fast shots.

&nbsp;

### Parameter 9: Reclosers.Shots read

This parameter gets the number of shots to lockout (fast + delayed).

&nbsp;

### Parameter 10: Reclosers.Shots write

This parameter sets the number of shots to lockout (fast + delayed).

&nbsp;

### Parameter 11: Reclosers.Open

This parameter open recloser's controlled element and lock out the recloser.

&nbsp;

### Parameter 12: Reclosers.Close

This parameter close the switched object controlled by the recloser. Resets recloser to first operation.

&nbsp;

### Parameter 13: Reclosers.Idx read

This parameter gets the active recloser by index into the recloser list. 1..Count.

&nbsp;

### Parameter 14: Reclosers.Idx write

This parameter sets the active recloser by index into the recloser list. 1..Count.

&nbsp;

### Parameter 15: Reclosers.Reset

This parameter resets the recloser to its normal state. If open, lock out the recloser. If closed, resets recloser to first operation.


***
_Created with the Standard Edition of HelpNDoc: [Make your documentation accessible on any device with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
