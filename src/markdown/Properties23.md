# Properties

&nbsp;

The properties of the RegControl object are as follows:

&nbsp;

| **Property** | **Description** |
| --- | --- |
| transformer | Name of Transformer element to which the RegControl is connected. Do not specify the full object name; "Transformer" is assumed for the object class. Example: Transformer=Xfmr1 |
| winding | Number of the winding of the transformer element that the RegControl is monitoring. 1 or 2, typically. Side Effect: Sets TAPWINDING property to the same winding. |
| vreg | Voltage regulator setting, in VOLTS, for the winding being controlled. Multiplying this value times the ptratio should yield the voltage across the WINDING of the controlled transformer. Default is 120.0 |
| band | Bandwidth in VOLTS for the controlled bus (see help for ptratio property). Default is 3.0 |
| delay | Time delay, in seconds, from when the voltage goes out of band to when the tap changing begins. This is used to determine which regulator control will act first. Default is 15. You may specify any floating point number to achieve a model of whatever condition is necessary. |
| ptratio | Ratio of the PT that converts the controlled winding voltage to the regulator voltage. Default is 60. If the winding is Wye, the line-to-neutral voltage is used. Else, the line-to-line voltage is used. |
| CTprim | Rating, in Amperes, of the primary CT rating for converting the line amps to control amps.The typical default secondary ampere rating is 0.2 Amps (check with manufacturer specs). |
| R | R setting on the line drop compensator in the regulator, expressed in VOLTS. |
| X | X setting on the line drop compensator in the regulator, expressed in VOLTS. |
| PTphase | For multi-phase transformers, the number of the phase being monitored or one of {MAX \| MIN} for all phases. Default=1. Must be less than or equal to the number of phases. Ignored for regulated bus. |
| tapwinding | Winding containing the actual taps, if different than the WINDING property. Defaults to the same winding as specified by the WINDING property. |
| bus | Name of a bus (busname.nodename) in the system to use as the controlled bus instead of the bus to which the transformer winding is connected or the R and X line drop compensator settings. Do not specify this value if you wish to use the line drop compensator settings. Default is null string. Assumes the base voltage for this bus is the same as the transformer winding base specified above. Note: This bus (1-phase) WILL BE CREATED by the regulator control upon SOLVE if not defined by some other device. You can specify the node of the bus you wish to sample (defaults to 1). If specified, the RegControl is redefined as a 1-phase device since only one voltage is used. |
| debugtrace | {Yes \| No\* } Default is no. Turn this on to capture the progress of the regulator model for each control iteration. Creates a separate file for each RegControl named "REG\_name.CSV". |
| EventLog | {Yes/True\* \| No/False} Default is YES for regulator control. Log control actions to Eventlog. |
| inversetime | {Yes \| No\* } Default is no. The time delay is adjusted inversely proportional to the amount the voltage is outside the band down to 10%. |
| maxtapchange | Maximum allowable tap change per control iteration in STATIC control mode. Default is 16. Set this to 1 to better approximate actual control action. Set this to 0 to fix the tap in the current position. |
| revband | Bandwidth for operating in the reverse direction. |
| revDelay | Time Delay in seconds (s) for executing the reversing action once the threshold for reversing has been exceeded. Default is 60 s. |
| reversible | {Yes \|No\*} Indicates whether the regulator has a reverse operation mode (associated settings must be defined). Default is No, which means the regulator forward settings apply for both forward and reverse power flow. Typically applies only to line regulators and not to LTC on a substation transformer.&nbsp; Use the "revNeutral", "idle", "idleReverse" and "idleForward" properties to define the desired operating mode: - Bi-directional: reversible=yes idle=yes/no (idling in the "no-load region" depends on the controller and is a functionality typically described in its datasheet) - Locked Forward: reversible=yes idleReverse=yes - Reverse Idle: reversible=yes idle=yes idleReverse=yes&nbsp; - Locked Reverse: reversible=yes idleForward=yes&nbsp; - Neutral Idle: reversible=yes revNeutral=yes idle=yes/no (idling in the "no-load region" depends on the controller and is a functionality typically described in its datasheet) |
| revNeutral | {Yes \| No\*} Default is no. Set this to Yes if you want the regulator to go to neutral in the reverse direction. |
| revR | R line drop compensator setting for reverse direction. |
| revThreshold | kW reverse power threshold for reversing the direction of the regulator. Default is 100.0 kw. |
| revvreg | Voltage setting in volts for operation in the reverse direction. |
| revX | X line drop compensator setting for reverse direction. |
| tapdelay | Delay in sec between tap changes. Default is 2. This is how long it takes between changes after the first change. |
| TapNum | An integer number indicating the tap position that the controlled transformer winding tap position is currently at, or is being set to. If being set, and the value is outside the range of the transformer min or max tap, then set to the min or max tap position as appropriate. Default is 0, which is the neutral tap. A conventional 32-step regulator has a range from -16 (Lower) to 16(Raise). With tap 0, there are actually 33 taps. You can query the tap position as follows:&nbsp; ? RegControl.MyRegulator.TapNum&nbsp; The result will go into the Result window or interface. |
| vlimit | Voltage Limit for bus to which regulated winding is connected (e.g. first customer). Default is 0.0. Set to a value greater then zero to activate this function. |
| LDC\_Z | Z value for Beckwith LDC\_Z control option. Volts adjustment at rated control current. |
| rev\_Z | Reverse Z value for Beckwith LDC\_Z control option. |
| RemotePTRatio | When regulating a bus (the Bus= property is set), the PT ratio required to convert actual voltage at the remote bus to control voltage. Is initialized to PTratio property. Set this property after setting PTratio. |
| Cogen | {Yes\|No\*} Default is No. The Cogen feature is activated. Continues looking forward if power reverses, but switches to reverse-mode LDC, vreg and band values. Optionally, use the "idle" property to specify if the regulator should idle in the "no-load region" (functionality typically described in the controller datasheet). |
| idle | {Yes\|No\*} Default is No. Enabling this property only has an effect when reversible or cogen properties are set to yes/true. For the "no-load region" where active power flow lies between -revThreshold and +revThreshold, the regulator will lock taps in the position they had before entering that region. Voltage override (Vlimit) takes priority.&nbsp; |
| idleReverse | {Yes\|No\*} Default is No. Similar to the "idle" property but applicable only when reversible=Yes (not for cogen mode) AND revNeutral=No. The regulator will lock taps in the position they had before entering the reverse flow zone. Voltage override (Vlimit) takes priority. |
| idleForward | {Yes\|No\*} Default is No. Similar to the "idle" property but applicable only when reversible=Yes (not for cogen mode). The regulator will lock taps in the position they had before entering the forward flow zone. Voltage override (Vlimit) takes priority. |



***
_Created with the Standard Edition of HelpNDoc: [Maximize Your PDF Protection with These Simple Steps](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
