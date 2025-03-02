# Properties

&nbsp;

The properties of the SwtControl are listed below:

&nbsp;

| **Property** | **Description** |
| --- | --- |
| Action | {Open \| Close} After specified delay time, and if not locked, causes the controlled switch to open or close. |
| basefreq | Base Frequency for ratings. |
| Delay | Operating time delay (sec) of the switch. Defaults to 120. |
| enabled | {Yes\|No or True\|False} Indicates whether this element is enabled. |
| like | Make like another object, e.g.: New Capacitor.C2 like=c1 ... |
| Lock | {Yes \| No} Delayed action. Sends CTRL\_LOCK or CTRL\_UNLOCK message to control queue. After delay time, controlled switch is locked in its present open / close state or unlocked. Switch will not respond to either manual (Action) or automatic (COM interface) control or internal OpenDSS Reset when locked. |
| Normal | {Open \| Closed\] Normal state of the switch. If not Locked, the switch reverts to this state for reset, change of mode, etc. Defaults to first Action or State specified if not specifically declared. |
| Reset | {Yes \| No} If Yes, forces Reset of switch to Normal state and removes Lock independently of any internal reset command for mode change, etc. |
| State | {Open \| Closed\] Present state of the switch. Upon setting, immediately forces state of switch. |
| SwitchedObj | Name of circuit element switch that the SwtControl operates. Specify the full object class and name. |
| SwitchedTerm | Terminal number of the controlled element switch. 1 or 2, typically. Default is 1. |



***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Spot and Fix Problems in Your Documentation with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
