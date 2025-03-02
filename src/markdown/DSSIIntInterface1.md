# DSSI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t DSSI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: DSS.NumCircuits

This parameter gets the number of circuits currently defined.

&nbsp;

### Parameter 1: DSS.ClearAll

This parameter clears all circuit definitions.

&nbsp;

### Parameter 2: DSS.ShowPanel

This parameter shows non-MDI child form of the Main DSS Edit form.

&nbsp;

### Parameter 3: DSS.Start

This parameter validates the user and start the DSS. Returns TRUE (1) if successful.

&nbsp;

### Parameter 4: DSS.NumClasses

This parameter gets the number of DSS intrinsic classes.

&nbsp;

### Parameter 5: DSS.NumUserClasses

This parameter gets the number of user-defined classes.

&nbsp;

### Parameter 6: DSS.Reset

This parameter resets DSS initialization for restarts, etc. from applets.

&nbsp;

### Parameter 7: DSS.AllowForms read

This parameter gets if the DSS allows forms (1) or not (0), default (1).

&nbsp;

### Parameter 8: DSS.AllowForms write

This parameter sets if the DSS allows forms (1) or not (0), default (1).


***
_Created with the Standard Edition of HelpNDoc: [Free help authoring environment](<https://www.helpndoc.com/help-authoring-tool>)_
