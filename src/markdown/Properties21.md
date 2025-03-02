# Properties

&nbsp;

The properties of the Fuse object are as follows:

&nbsp;

| **Property** | **Description** |
| --- | --- |
| (1) MonitoredObj | Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Fuse is connected. This is the "monitored" element. There is no default; must be specified. |
| (2) MonitoredTerm | Number of the terminal of the circuit element to which the Fuse is connected. 1 or 2, typically. Default is 1. |
| (3) SwitchedObj | Name of circuit element switch that the Fuse controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element. |
| (4) SwitchedTerm | Number of the terminal of the controlled element in which the switch is controlled by the Fuse. 1 or 2, typically. Default is 1. Assumes all phases of the element have a fuse of this type. |
| (5) FuseCurve | Name of the TCC Curve object that determines the fuse blowing. Must have been previously defined as a TCC\_Curve object. Default is "Tlink". Multiplying the current values in the curve by the "RatedCurrent" value gives the actual current. |
| (6) RatedCurrent | Multiplier or actual phase amps for the phase TCC curve. Defaults to 1.0. |
| (7) Delay | Fixed delay time (sec) added to Fuse blowing time determined from the TCC curve. Default is 0.0. Used to represent fuse clearing time or any other delay. |
| (8) Action | {Trip/Open \| Close} Action that overrides the Fuse control. Simulates manual control on Fuse "Trip" or "Open" causes the controlled element to open and lock out. "Close" causes the controlled element to close and the Fuse to reset. |
| (9) basefreq | Base Frequency for ratings. |
| (10) enabled | {Yes\|No or True\|False} Indicates whether this element is enabled. |



***
_Created with the Standard Edition of HelpNDoc: [Create cross-platform Qt Help files](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
