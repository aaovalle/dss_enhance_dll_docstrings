# SolutionS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr SolutionS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string according to the number sent in the variable “parameter”. The parameter can be one of the following:

&nbsp;

### Parameter 0: Solution.ModeID

This parameter returns the ID (text) of the present solution mode.

&nbsp;

### Parameter 1: Solution.LDCurve read

This parameter returns the Load-Duration Curve name for LD modes.

&nbsp;

### Parameter 2: Solution.LDCurve write

This parameter sets the Load-Duration Curve name for LD modes.

&nbsp;

### Parameter 3: Solution.DefaultDaily read

This parameter returns the default daily load shape (defaults to "Default").

&nbsp;

### Parameter 4: Solution.DefaultDaily write

This parameter sets the default daily load shape (defaults to "Default").

&nbsp;

### Parameter 5: Solution.DefaultYearly read

This parameter returns the default yearly load shape (defaults to "Default").

&nbsp;

### Parameter 6: Solution.DefaultYearly write

This parameter sets the default yearly load shape (defaults to "Default").


***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
