# Properties

&nbsp;

The following are the properties associated to the relay object:

&nbsp;

| **Property** | **Description** |
| --- | --- |
| (1) MonitoredObj | Full object name of the circuit element, typically a line, transformer, load, or generator, to which the relay's PT and/or CT are connected. This is the "monitored" element. There is no default; must be specified. |
| (2) MonitoredTerm | Number of the terminal of the circuit element to which the Relay is connected. 1 or 2, typically. Default is 1. |
| (3) SwitchedObj | Name of circuit element switch that the Relay controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element. |
| (4) SwitchedTerm | Number of the terminal of the controlled element in which the switch is controlled by the Relay. 1 or 2, typically. Default is 1. |
| (5) type | One of a legal relay type:&nbsp; Current Voltage ReversePower 46 (neg seq current) 47 (neg seq voltage) Generic (generic over/under relay)&nbsp; Default is overcurrent relay (Current) Specify the curve and pickup settings appropriate for each type. Generic relays monitor PC Element Control variables and trip on out of over/under range in definite time |
| (6) Phasecurve | Name of the TCC Curve object that determines the phase trip. Must have been previously defined as a TCC\_Curve object. Default is none (ignored). For overcurrent relay, multiplying the current values in the curve by the "phasetrip" value gives the actual current. |
| (7) Groundcurve | Name of the TCC Curve object that determines the ground trip. Must have been previously defined as a TCC\_Curve object. Default is none (ignored).For overcurrent relay, multiplying the current values in the curve by the "groundtrip" valuw gives the actual current. |
| (8) PhaseTrip | Multiplier or actual phase amps for the phase TCC curve. Defaults to 1.0. |
| (9) GroundTrip | Multiplier or actual ground amps (3I0) for the ground TCC curve. Defaults to 1.0. |
| (10) TDPhase | Time dial for Phase trip curve. Multiplier on time axis of specified curve. Default=1.0. |
| (11) TDGround | Time dial for Ground trip curve. Multiplier on time axis of specified curve. Default=1.0. |
| (12) PhaseInst | Actual amps (Current relay) or kW (reverse power relay) for instantaneous phase trip which is assumed to happen in 0.01 sec + Delay Time. Default is 0.0, which signifies no inst trip. Use this value for specifying the Reverse Power threshold (kW) for reverse power relays. |
| (13) GroundInst | Actual amps for instantaneous ground trip which is assumed to happen in 0.01 sec + Delay Time.Default is 0.0, which signifies no inst trip. |
| (14) Reset | Reset time in sec for relay. Default is 15. If |
| (15) Shots | Number of shots to lockout. Default is 4. This is one more than the number of reclose intervals. |
| (16) RecloseIntervals | Array of reclose intervals. If none, specify "NONE". Default for overcurrent relay is (0.5, 2.0, 2.0) seconds. Default for a voltage relay is (5.0). In a voltage relay, this is seconds after restoration of voltage that the reclose occurs. Reverse power relay is one shot to lockout, so this is ignored. A locked out relay must be closed manually (set action=close). |
| (17) Delay | Trip time delay (sec) for definite time relays. Default is 0.0 for current and voltage relays. If \>0 then this value is used instead of curves. Used exclusivelyby RevPower, 46 and 47 relays at this release. Defaults to 0.1 s for these relays. |
| (18) Overvoltcurve | TCC Curve object to use for overvoltage relay. Curve is assumed to be defined with per unit voltage values. Voltage base should be defined for the relay. Default is none (ignored). |
| (19) Undervoltcurve | TCC Curve object to use for undervoltage relay. Curve is assumed to be defined with per unit voltage values. Voltage base should be defined for the relay. Default is none (ignored). |
| (20) kvbase | Voltage base (kV) for the relay. Specify line‐line for 3 phase devices); lineneutral for 1‐phase devices. Relay assumes the number of phases of the monitored element. Default is 0.0, which results in assuming the voltage values in the "TCC" curve are specified in actual line‐to‐neutral volts. |
| (21) 47%Pickup | Percent voltage pickup for 47 relay (Neg seq voltage). Default is 2. Specify also base voltage (kvbase) and delay time value. |
| (22) 46BaseAmps | Base current, Amps, for 46 relay (neg seq current). Used for establishing pickup and per unit I‐squared‐t. |
| (23) 46%Pickup | Percent pickup current for 46 relay (neg seq current). Default is 20.0. When current exceeds this value \* BaseAmps, I‐squared‐t calc starts. |
| (24) 46isqt | Negative Sequence I‐squared‐t trip value for 46 relay (neg seq current). Default is 1 (trips in 1 sec for 1 per unit neg seq current). Should be 1 to 99. |
| (25) Variable | Name of variable in PC Elements being monitored. Only applies to Generic relay. |
| (26) overtrip | Trip setting (high value) for Generic relay variable. Relay trips in definite time if value of variable exceeds this value. |
| (27) undertrip | Trip setting (low value) for Generic relay variable. Relay trips in definite time if value of variable is less than this value. |
| (28) Breakertime | Fixed delay time (sec) added to relay time. Default is 0.0. Designed to represent breaker time or some other delay after a trip decision is made.Use Delay\_Time property for setting a fixed trip time delay.Added to trip time of current and voltage relays. Could use in combination with inst trip value to obtain a definite time overcurrent relay. |
| (29) action | {Trip/Open \| Close} Action that overrides the relay control. Simulates manual control on breaker. "Trip" or "Open" causes the controlled element to open and lock out. "Close" causes the controlled element to close and the relay to reset to its first operation. |
| (30) basefreq | Base Frequency for ratings. |
| (31) enabled | {Yes\|No or True\|False} Indicates whether this element is enabled. |



***
_Created with the Standard Edition of HelpNDoc: [Make the switch to CHM with HelpNDoc's hassle-free WinHelp HLP to CHM conversion tool](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
