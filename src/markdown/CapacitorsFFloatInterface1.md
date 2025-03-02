# CapacitorsF (Float) Interface

&nbsp;

This interface can be used to read/modify the properties of the Capacitors Class where the values are doubles. The structure of the interface is as follows:

&nbsp;

double CapacitorsF(int32\_t Parameter, double argument) ;

&nbsp;

This interface returns a floating point number (64 bits), the variable “parameter” is used to specify the property of the class to be used and the variable “argument” can be used to modify the value of the property when necessary. Reading and writing properties are separated and require a different parameter number to be executed.

&nbsp;

The properties (parameter) are integer numbers and are described as follows:

&nbsp;

### Parameter 0: Capacitors.kV read

This parameter gets the bank rating. Use LL for 2 or 3 phases, or actual can rating for 1 phase.

&nbsp;

### Parameter 1: Capacitors.kV write

This parameter sets the bank rating. Use LL for 2 or 3 phases, or actual can rating for 1 phase.

&nbsp;

### Parameter 2: Capacitors.kvar read

This parameter gets the total bank kvar, distributed equally among phases and steps.

&nbsp;

### Parameter 3: Capacitors.kvar write

This parameter sets the total bank kvar, distributed equally among phases and steps.


***
_Created with the Standard Edition of HelpNDoc: [Import and export Markdown documents](<https://www.helpndoc.com/feature-tour/markdown-import-export-using-helpndoc-help-authoring-tool/>)_
