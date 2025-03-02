# DSS_ExecutiveS (Float) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr DSSExecutiveS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Executive.Command

This parameter gets i-th command (specified in the argument as string).

&nbsp;

### Parameter 1: Executive.Option

This parameter gets i-th option (specified in the argument as string).

&nbsp;

### Parameter 2: Executive.CommandHelp

This parameter gets help string for i-th command (specified in the argument as string).

&nbsp;

### Parameter 3: Executive.OptionHelp

This parameter gets help string for i-th option (specified in the argument as string).

&nbsp;

### Parameter 4: Executive.OptionValue

This parameter gets present value for i-th option (specified in the argument as string).


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Edit and Export Markdown Documents](<https://www.helpndoc.com/feature-tour/markdown-import-export-using-helpndoc-help-authoring-tool/>)_
