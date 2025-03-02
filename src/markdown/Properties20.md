# Properties

&nbsp;

The properties of the CapControl object are as follows:

&nbsp;

| **Property** | **Description** |
| --- | --- |
| *Element* | Full object name of the circuit element, typically a line or transformer, to which the capacitor control's PT and/or CT are connected.There is no default; must be specified. |
| *Capacitor* | Name of Capacitor element which the CapControl controls. No Default; Must be specified.Do not specify the full object name; "Capacitor" is assumed for the object class. Example: Capacitor=cap1 |
| *Type* | {Current \| voltage \| kvar \| PF \| time } Control type. Specify the ONsetting and OFFsetting appropriately with the type of control. (See help for ONsetting) |
| *CTPhase* | Number of the phase being monitored for CURRENT control or one of {AVG \| MAX \| MIN} for all phases. Default=1. If delta or L-L connection, enter the first or the two phases being monitored \[1-2, 2-3, 3-1\]. Must be less than the number of phases. Does not apply to kvar control which uses all phases by default. |
| *CTratio* | Ratio of the CT from line amps to control ampere setting for current and kvar control types. |
| *DeadTime* | Dead time after capacitor is turned OFF before it can be turned back ON. Default is 300 sec. |
| *Delay* | Time delay, in seconds, from when the control is armed before it sends out the switching command to turn ON. The control may reset before the action actually occurs. This is used to determine which capacity control will act first. Default is 15. You may specify any floating point number to achieve a model of whatever condition is necessary. |
| *DelayOFF* | Time delay, in seconds, for control to turn OFF when present state is ON. Default is 15. |
| *EventLog* | {Yes/True\* \| No/False} Default is YES for CapControl. Log control actions to Eventlog. |
| *OFFsetting* | Value at which the control arms to switch the capacitor OFF. (See help for ONsetting)For Time control, is OK to have Off time the next day ( \< On time) |
| *ONsetting* | Value at which the control arms to switch the capacitor ON (or ratchet up a step). &nbsp; Type of Control:&nbsp; Current: Line Amps / CTratio Voltage: Line-Neutral (or Line-Line for delta) Volts / PTratio kvar: Total kvar, all phases (3-phase for pos seq model). This is directional. PF: Power Factor, Total power in monitored terminal. Negative for Leading. Time: Hrs from Midnight as a floating point number (decimal). 7:30am would be entered as 7.5. |
| *PTPhase* | Number of the phase being monitored for VOLTAGE control or one of {AVG \| MAX \| MIN} for all phases. Default=1. If delta or L-L connection, enter the first or the two phases being monitored \[1-2, 2-3, 3-1\]. Must be less than the number of phases. Does not apply to kvar control which uses all phases by default. |
| *PTratio* | Ratio of the PT that converts the monitored voltage to the control voltage. Default is 60. If the capacitor is Wye, the 1st phase line-to-neutral voltage is monitored. Else, the line-to-line voltage (1st - 2nd phase) is monitored. |
| *terminal* | Number of the terminal of the circuit element to which the CapControl is connected. 1 or 2, typically. Default is 1. |
| *VBus* | Name of bus to use for voltage override function. Default is bus at monitored terminal. Sometimes it is useful to monitor a bus in another location to emulate various DMS control algorithms. |
| *Vmax* | Maximum voltage, in volts. If the voltage across the capacitor divided by the PTRATIO is greater than this voltage, the capacitor will switch OFF regardless of other control settings. Default is 126 (goes with a PT ratio of 60 for 12.47 kV system). |
| *Vmin* | Minimum voltage, in volts. If the voltage across the capacitor divided by the PTRATIO is less than this voltage, the capacitor will switch ON regardless of other control settings. Default is 115 (goes with a PT ratio of 60 for 12.47 kV system). |
| *VoltOverride* | {Yes \| No} Default is No. Switch to indicate whether VOLTAGE OVERRIDE is to be considered. Vmax and Vmin must be set to reasonable values if this property is Yes. |


&nbsp;

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Quickly and Easily Convert Your Word Document to an ePub or Kindle eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
