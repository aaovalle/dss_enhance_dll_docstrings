# TolopolgyS (String) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

CStr TopologyS(int32\_t Parameter, CStr Argument);

&nbsp;

This interface returns a string with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Topology.BranchName read

This parameter gets the name of the active branch.

&nbsp;

### Parameter 1: Topology.BranchName write

This parameter sets the name of the active branch.

&nbsp;

### Parameter 2: Topology.BusName read

This parameter gets the name of the active Bus.

&nbsp;

### Parameter 3: Topology.BusName write

This parameter sets the Bus active by name.


***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
