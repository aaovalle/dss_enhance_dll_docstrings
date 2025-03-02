# GICSourcesI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t GICSourcesI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: GICSources.Count

This parameter gets number of GICSources in active circuit.

&nbsp;

### Parameter 1: GICSources.First

This parameter sets the first GICSource active. Returns 0 if none.

&nbsp;

### Parameter 2: GICSources.Next

This parameter sets the next GICSource active. Returns 0 if none.

&nbsp;

### Parameter 3: GICSources.Phases read

This parameter returns the number of phases of the active GICSource.

&nbsp;

### Parameter 4: GICSources.Phases write

This parameter allows to specify the number of phases of the active GICSource.


***
_Created with the Standard Edition of HelpNDoc: [HelpNDoc's Project Analyzer: Incredible documentation assistant](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
