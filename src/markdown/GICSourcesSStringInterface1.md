# GICSourcesS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr GISSourcesS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: GICSources.Bus1

This parameter gets the name of the first bus name of GICSource (Created name).

&nbsp;

### Parameter 1: GICSources.Bus2

This parameter gets the name of the  second bus name of GICSource (Created name).

&nbsp;

### Parameter 2: GICSources.Name read

This parameter gets the name of the active GICSource object.

&nbsp;

### Parameter 3: GICSources.Name write

This parameter sets the name of the active GICSource object.


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Review with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
