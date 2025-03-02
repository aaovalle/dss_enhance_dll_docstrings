# Properties

&nbsp;

The properties for the fault object are as follows:

&nbsp;

&nbsp;

&nbsp;

| **Property** | **Description** |
| --- | --- |
| phases | Number of Phases. Default is 1. |
| bus1 | Name of first bus. Examples:&nbsp; bus1=busname bus1=busname.1.2.3 |
| bus2 | Name of 2nd bus. Defaults to all phases connected to first bus, node 0, if not specified. (Shunt Wye to ground connection) |
| R | Resistance, each phase, ohms. Default is 0.0001. Assumed to be Mean value if gaussian random mode.Max value if uniform mode. A Fault is actually a series resistance that defaults to a wye connection to ground on the second terminal. You may reconnect the 2nd terminal to achieve whatever connection. Use the Gmatrix property to specify an arbitrary conductance matrix. |
| Gmatrix | Use this to specify a nodal conductance (G) matrix to represent some arbitrary resistance network. Specify in lower triangle form as usual for DSS matrices. |
| MinAmps | Minimum amps that can sustain a temporary fault. Default is 5. |
| ONtime | Time (sec) at which the fault is established for time varying simulations. Default is 0.0 (on at the beginning of the simulation) |
| pctperm | Percent of failures that become permanent. (not currently used) |
| Temporary | {Yes \| No} Default is No. Designate whether the fault is temporary. For Time-varying simulations, the fault will be removed if the current through the fault drops below the MINAMPS criteria. |
| %stddev | Percent standard deviation in resistance to assume for Monte Carlo fault (MF) solution mode for GAUSSIAN distribution. Default is 0 (no variation from mean). |


&nbsp;

Standard Inherited Properties (may not apply to all Fault elements)

&nbsp;

| **Property** | **Description** |
| --- | --- |
| normamps | Normal rated current. |
| emergamps | Maximum current. |
| basefreq | Base Frequency for ratings. |
| faultrate | No. of failures per year. This property can be used by such things as a monte carlo fault study to specify how often this fault is likely to occur. |
| repair | Hours to repair. |
| enabled | {Yes\|No or True\|False} Indicates whether this element is enabled. |
| like | Make like another object, e.g.:&nbsp; New Fault.F2 like=F1 ... |


&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Capabilities with HelpNDoc's User-Friendly UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
