# Reduction Options

&nbsp;

The algorithms for circuit reduction are implemented as part of the EnergyMeter object. This is the only, or one of the few, objects that organizes the branches into radial zones. The reduction actions are executed by the Reduce command. This reduces the circuit in memory. To save the results, you must save the circuit.

&nbsp;

Set ReduceOption = default

&nbsp;

•Drops dangling ends

•Eliminates intermediate buses without loads or capacitors or lateral taps.

&nbsp;

Set ReduceOption=Stubs \[Zmag=0.02\]

&nbsp;

•Merges very short lines in with either the parent branch or the child branch

•Based on the impedance of the branch

&nbsp;

Set ReduceOption = BreakLoops

&nbsp;

•Breaks open the loops found in the meter zone by disabling one of the lines.

•Thus, the loop will be fed by only one.

&nbsp;

Set ReduceOption = MergeParallel

&nbsp;

•Merges lines that have been found to be in parallel between the same two buses.

&nbsp;

Set ReduceOption=Tapends \[maxangle=15\]

&nbsp;

•Eliminates all buses except those at taps and the feeder ends,and where the feeder turns by greater than maxangle degrees.

•Coordinates must be defined for the latter to be effective.

&nbsp;

Marking buses with "Keeplist" will prevent their elimination. Recommended format for large circuits:

&nbsp;

Set Keeplist=(file=filenamelist.txt)

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Ease of Use of a Help Authoring Tool](<https://www.helpndoc.com>)_
