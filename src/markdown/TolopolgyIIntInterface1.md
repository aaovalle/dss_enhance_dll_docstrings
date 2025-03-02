# TolopolgyI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t TopologyI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Topology.NumLoops

This parameter gets the number of loops.

&nbsp;

### Parameter 1: Topology.NumIsolatedBranches

This parameter gets the number of isolated branches (PD elements and capacitors).

&nbsp;

### Parameter 2: Topology.NumIsolatedLoads

This parameter gets the number of isolated loads.

&nbsp;

### Parameter 3: Topology.First

This parameter sets the first branch active, returns 0 if none.

&nbsp;

### Parameter 4: Topology.Next

This parameter sets the next branch active, returns 0 if none.

&nbsp;

### Parameter 5: Topology.ActiveBranch

This parameter returns the index of the active Branch.

&nbsp;

### Parameter 6: Topology.ForwardBranch

This parameter moves forward in the tree, return index of new active branch or 0 if no more.

&nbsp;

### Parameter 7: Topology.BackwardBranch

This parameter moves back toward the source, return index of new active branch or 0 if no more.

&nbsp;

### Parameter 8: Topology.LoopedBranch

This parameter moves to looped branch, return index or 0 if none.

&nbsp;

### Parameter 9: Topology.ParallelBranch

This parameter mode to directly parallel branch, return index or 0 if none.

&nbsp;

### Parameter 10: Topology.FirstLoad

This parameter sets as active load the first load at the active branch, return index or 0 if none.

&nbsp;

### Parameter 11: Topology.NextLoad

This parameter sets as active load the next load at the active branch, return index or 0 if none.

&nbsp;

### Parameter 12: Topology.ActiveLevel

This parameter gets the topological depth of the active branch.


***
_Created with the Standard Edition of HelpNDoc: [Simplify Your Help Documentation Process with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
