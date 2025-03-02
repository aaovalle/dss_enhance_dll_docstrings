# Properties

&nbsp;

The properties of the recloser object included in OpenDSS are as follows:

&nbsp;

&nbsp;

| **Property** | **Description** |
| --- | --- |
| (1) MonitoredObj | Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Recloser's PT and/or CT are connected. This is the "monitored" element. There is no default; must be specified. |
| (2) MonitoredTerm | Number of the terminal of the circuit element to which the Recloser is connected. 1 or 2, typically. Default is 1. |
| (3) SwitchedObj | Name of circuit element switch that the Recloser controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element. |
| (4) SwitchedTerm | Number of the terminal of the controlled element in which the switch is controlled by the Recloser. 1 or 2, typically. Default is 1. |
| (5) NumFast | Number of Fast (fuse saving) operations. Default is 1. (See "Shots") |
| (6) PhaseFast | Name of the TCC Curve object that determines the Phase Fast trip. Must have been previously defined as a TCC\_Curve object. Default is "A". Multiplying the current values in the curve by the "phasetrip" value gives the actual current. |
| (7) PhaseDelayed | Name of the TCC Curve object that determines the Phase Delayed trip. Must have been previously defined as a TCC\_Curve object. Default is "D".Multiplying the current values in the curve by the "phasetrip" value gives the actual current. |
| (8) GroundFast | Name of the TCC Curve object that determines the Ground Fast trip. Must have been previously defined as a TCC\_Curve object. Default is none (ignored). Multiplying the current values in the curve by the "groundtrip" value gives the actual current. |
| (9) GroundDelayed | Name of the TCC Curve object that determines the Ground Delayed trip. Must have been previously defined as a TCC\_Curve object. Default is none (ignored).Multiplying the current values in the curve by the "groundtrip" value gives the actual current. |
| (10) PhaseTrip | Multiplier or actual phase amps for the phase TCC curve. Defaults to 1.0. |
| (11) GroundTrip | Multiplier or actual ground amps (3I0) for the ground TCC curve. Defaults to 1.0. |
| (12) PhaseInst | Actual amps for instantaneous phase trip which is assumed to happen in 0.01 sec + Delay Time. Default is 0.0, which signifies no inst trip. |
| (13) GroundInst | Actual amps for instantaneous ground trip which is assumed to happen in 0.01 sec + Delay Time.Default is 0.0, which signifies no inst trip. |
| (14) Reset | Reset time in sec for Recloser. Default is 15. |
| (15) Shots | Total Number of fast and delayed shots to lockout. Default is 4. This is one more than the number of reclose intervals. |
| (16) RecloseIntervals | Array of reclose intervals. Default for Recloser is (0.5, 2.0, 2.0) seconds. A locked out Recloser must be closed manually (action=close). |
| (17) Delay | Fixed delay time (sec) added to Recloser trip time. Default is 0.0. Used to represent breaker time or any other delay. |
| (18) Action | {Trip/Open \| Close} Action that overrides the Recloser control. Simulates manual control on recloser "Trip" or "Open" causes the controlled element to open and lock out. "Close" causes the controlled element to close and the Recloser to reset to its first operation. |
| (19) TDPhFast | Time dial for Phase Fast trip curve. Multiplier on time axis of specified curve. Default=1.0. |
| (20) TDGrFast | Time dial for Ground Fast trip curve. Multiplier on time axis of specified curve. Default=1.0. |
| (21) TDPhDelayed | Time dial for Phase Delayed trip curve. Multiplier on time axis of specified curve. Default=1.0. |
| (22) TDGrDelayed | Time dial for Ground Delayed trip curve. Multiplier on time axis of specified curve. Default=1.0. |
| (23) basefreq | Base Frequency for ratings. |
| (24) enabled | {Yes\|No or True\|False} Indicates whether this element is enabled. |
| (25) like |  |



***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Documentation with HelpNDoc's Project Analyzer Features](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
