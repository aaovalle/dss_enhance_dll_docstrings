# DSSS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr DSSS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: DSS.NewCircuit

This parameter makes a new circuit, the name of the circuit must be specified in the Argument.

&nbsp;

### Parameter 1: DSS.Version

This parameter gets the version string for the DSS.

&nbsp;

### Parameter 2: DSS.DataPath read

This parameter gets the Data File Path. Default for reports, etc. from DSS.

&nbsp;

### Parameter 3: DSS.DataPath write

This parameter sets the Data File Path. Default for reports, etc. from DSS.

&nbsp;

### Parameter 4: DSS.DefaultEditor

This parameter gets the path name for the default text editor.


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Spot and Fix Problems in Your Documentation with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
