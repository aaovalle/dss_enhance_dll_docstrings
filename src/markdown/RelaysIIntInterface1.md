# RelaysI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t RelaysI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Relays.Count

This parameter gets number of Relays in active circuit.

&nbsp;

### Parameter 1: Relays.First

This parameter sets first relay active. If none, returns 0.

&nbsp;

### Parameter 2: Relays.Next

This parameter sets next relay active. If none, returns 0.

&nbsp;

### Parameter 3: Relays.MonitoredTerm read

This parameter gets the number of terminal of monitored element that this relay is monitoring.

&nbsp;

### Parameter 4: Relays.MonitoredTerm write

This parameter sets the number of terminal of monitored element that this relay is monitoring.

&nbsp;

### Parameter 5: Relays.SwitchedTerm read

This parameter gets the number of terminal of the switched object that will be opened when the relay trips.

&nbsp;

### Parameter 6: Relays.SwitchedTerm write

This parameter sets the number of terminal of the switched object that will be opened when the relay trips.

&nbsp;

### Parameter 7: Relays.Idx read

This parameter gets the active relay by index into the Relay list. 1..Count.

&nbsp;

### Parameter 8: Relays.Idx write

This parameter sets the active relay by index into the Relay list. 1..Count.

&nbsp;

### Parameter 9: Relays.Open

This parameter opens recloser's controlled element and lock out the relay.

&nbsp;

### Parameter 10: Relays.Close

This parameter closes the switched object controlled by the relay. Resets relay to first operation.

&nbsp;

### Parameter 11: Relays.Reset

This parameter resets the relay to its normal state. If open, lock out the relay. If closed, resets relay to first operation.


***
_Created with the Standard Edition of HelpNDoc: [Don't be left in the past: convert your WinHelp HLP help files to CHM with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
