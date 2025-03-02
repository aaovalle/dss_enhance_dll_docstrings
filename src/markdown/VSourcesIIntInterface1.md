# VSourcesI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t VSourcesI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: VSources.Count

This parameter returns the number of VSource objects currently defined in the active circuit.

&nbsp;

### Parameter 1: VSources.First

This parameter sets the first VSource to be active; returns 0 if none.

&nbsp;

### Parameter 2: VSources.Next

This parameter sets the next VSource to be active; returns 0 if none.

&nbsp;

### Parameter 3: VSources.Phases read

This parameter gets the number of phases of the active VSource.

&nbsp;

### Parameter 4: VSources.Phases write

This parameter sets the number of phases of the active VSource.


***
_Created with the Standard Edition of HelpNDoc: [Import and export Markdown documents](<https://www.helpndoc.com/feature-tour/markdown-import-export-using-helpndoc-help-authoring-tool/>)_
