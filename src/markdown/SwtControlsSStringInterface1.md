# SwtControlsS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr SwtControlsS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: SwtControls.Name read

This parameter gets the name of the active SwtControl.

&nbsp;

### Parameter 1: SwtControls.Name write

This parameter sets a SwtControl active by name.

&nbsp;

### Parameter 2: SwtControls.SwitchedObj read

This parameter gets the name of the switched object by the active SwtControl.

&nbsp;

### Parameter 3: SwtControls.SwitchedObj write

This parameter sets the switched object by name.


***
_Created with the Standard Edition of HelpNDoc: [Powerful and User-Friendly Help Authoring Tool for Markdown Documents](<https://www.helpndoc.com/feature-tour/markdown-import-export-using-helpndoc-help-authoring-tool/>)_
