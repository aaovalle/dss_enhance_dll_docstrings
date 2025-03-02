# Properties

[Table 3](<OpenDSSDocumentation.md#\_bookmark36>) lists all available properties of the StorageController element.

Table 3: Properties of the StorageController element

| **Property** | **Description** |
| --- | --- |
| *(1) Element* | Full object name of the circuit element, typically a line or transformer, which the control is monitoring. There is no default; Must be specified. |
| *(2) Terminal* | Number of the terminal of the circuit element to which the StorageCon- troller control is connected. 1 or 2, typically. Default is 1. Make sure to select the proper direction on the power for the respective dispatch mode. |
|  &nbsp; *(3) MonPhase* | Number of the phase being monitored or one of *{*&#8202;AVG#8202;*\|*&#8202;MAX#8202;*\|*&#8202;MIN#8202;*}* for all phases. Default=MAX. Must be less than the number of phases. Used in PeakShave, Follow, Support and I-PeakShave discharging modes and in PeakShaveLow, I-PeakShaveLow charging modes. For modes based on active power measurements, the value used by the control is the monitored one multiplied by the number of phases of the monitored element. |
|  *(4) kWTarget* | kW/kamps target for Discharging. The storage element fleet is dis- patched to try to hold the power/current in band at least until the storage is depleted. The selection of power or current depends on the Discharge mode (PeakShave *→* kW, I-PeakShave *→* kamps). |
|  *(5) kWTargetLow* | kW/kamps target for Charging. The storage element fleet is dispatched to try to hold the power/current in band at least until the storage is fully charged. The selection of power or current depends on the charge. mode (PeakShavelow *→* kW, I-PeakShavelow*→* kamps). |
|  *(6) %kWBand* | Bandwidth (% of Target kW/kamps) of the dead band around the kW/kamps target value. Default is 2% (+/-1%). No dispatch changes are attempted if the power in the monitored terminal stays within this band. |
|  *(7) kWBand* | Alternative way of specifying the bandwidth. (kW/kamps) of the dead band around the kW/kamps target value. Default is 2% of kWTar- get (+/-1%). No dispatch changes are attempted if the power in the monitored terminal stays within this band. |
|  *(8) %kWBandLow* | Bandwidth (% of kWTargetLow) of the dead band around the kW/kamps low target value. Default is 2% (+/-1%). No charging is attempted if the power in the monitored terminal stays within this band. |
|  *(9) kWBandLow* | Alternative way of specifying the bandwidth. (kW/kamps) of the dead band around the kW/kamps low target value. Default is 2% of kW- TargetLow (+/-1%). No charging is attempted if the power in the monitored terminal stays within this band. |


| *(10) ElementList* | Array list of Storage elements to be controlled. If not specified, all storage elements in the circuit not presently dispatched by another controller are assumed dispatched by this controller. |
| --- | --- |
|  *(11) Weights* | Array of proportional weights corresponding to each storage element in the ElementList. The needed kW or kvar to get back to center band is dispatched to each storage element according to these weights. Default is to set all weights to 1.0. |
|  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; *(12) ModeDischarge* | *{*&#8202;PeakShave\**\|*&#8202;Follow#8202;*\|*&#8202;Support#8202;*\|*&#8202;Loadshape#8202;*\|*&#8202;Time#8202;*\|*&#8202;Schedule#8202;*\|*&#8202;I-PeakShave#8202;*}* Mode of operation for the DISCHARGE FUNCTION of this con- troller. In PeakShave mode (Default), the control attempts to discharge storage to keep power in the monitored element below the kWTarget. In Follow mode, the control is triggered by time and resets the kWTarget value to the present monitored element power. It then attempts to discharge storage to keep power in the monitored element below the new kWTarget. See TimeDischargeTrigger. In Support mode, the control operates oppositely of PeakShave mode: storage is discharged to keep kW power output up near the target. In Loadshape mode, both charging and discharging precisely follows the per unit loadshape. Storage is discharged when the loadshape value is positive. In Time mode, the storage discharge is turned on at the specified %RatekW at the specified discharge trigger time in fractional hours. In Schedule mode, the Tup, TFlat, and Tdn properties specify the up ramp duration, flat duration, and down ramp duration for the schedule. The schedule start time is set by TimeDischargeTrigger and the rate of discharge for the flat part is determined by %RatekW. In I-PeakShave mode, the control attempts to discharge storage to keep current in the monitored element below the target given in k-amps (thousands of amps), when this control mode is active, the property kWTarget will be expressed in k-amps. |


|  &nbsp; &nbsp; &nbsp; &nbsp; *(13) ModeCharge* | *{*&#8202;Loadshape#8202;*\|*&#8202;Time\**\|*&#8202;PeakShaveLow#8202;*\|*&#8202;I-PeakShaveLow#8202;*}* Mode&nbsp; of&nbsp; opera- tion for the CHARGE FUNCTION of this controller. In Loadshape mode, both charging and discharging precisely follows the per unit loadshape. Storage is charged when the loadshape value is negative. In Time mode, the storage charging FUNCTION is triggered at the specified %RateCharge at the specified charge trigger time in frac- tional hours. In PeakShaveLow mode, the charging operation will charge the storage fleet when the power at a monitored element is below a specified KW target (kWTarget low). The storage will charge as much power as nec- essary to keep the power within the deadband around kWTarget low. In I-PeakShaveLow mode, the charging operation will charge the stor- age fleet when the current (Amps) at a monitored element is below a specified amps target (kWTarget low). The storage will charge as much power as necessary to keep the amps within the deadband around kWTarget low. When this control mode is active, the property kW- Target low will be expressed in k-amps and all the other parameters will be adjusted to match the amps (current) control criteria. |
| --- | --- |
| &nbsp; *(14) TimeDischargeTrigger* | Default time of day (hr) for initiating Discharging of the fleet. During Follow or Time mode discharging is triggered at a fixed time each day at this hour. If Follow mode, storage will be discharged to attempt to hold the load at or below the power level at the time of triggering. In Time mode, the discharge is based on the %RatekW property value. Set this to a negative value to ignore. Default is 12.0 for Follow mode; otherwise it is -1 (ignored). |
|  *(15) TimeChargeTrigger* | Default time of day (hr) for initiating charging in Time control mode. Set this to a negative value to ignore. Default is 2.0. (0200). When this value is *\>*&#8202;0 the storage fleet is set to charging at this time regardless of other control criteria to make sure storage is topped off for the next discharge cycle. |
| *(16) %RatekW* | Sets the kW discharge rate in % of rated capacity for each element of the fleet. Applies to TIME control mode, SCHEDULE mode, or anytime discharging is triggered by time. |
| *(17) %RateCharge* | Sets the kW charging rate in % of rated capacity for each element of the fleet. Applies to TIME control mode and anytime charging mode is entered due to a time trigger. |
|  *(18) %Reserve* | Use this property to change the % reserve for each storage element under control of this controller. This might be used, for example, to allow deeper discharges of storage or in case of emergency operation to use the remainder of the storage element. |


| *(19) kWhTotal* | (Read only). Total rated kWh energy storage capacity of storage ele- ments controlled by this controller. |
| --- | --- |
| *(20) kWTotal* | (Read only). Total rated kW power capacity of storage elements con- trolled by this controller. |
| *(21) kWhActual* | (Read only). Actual kWh stored of all controlled storage elements. |
| *(22) kWActual* | (Read only). Actual kW output of all controlled storage elements. |
| *(23) kWneed* | (Read only). KW needed to meet target. |
| *(24) Yearly* | Dispatch loadshape object, If any, for Yearly solution Mode. |
| *(25) Daily* | Dispatch loadshape object, If any, for Daily solution mode. |
| *(26) Duty* | Dispatch loadshape object, If any, for Dutycycle solution mode. |
| *(27) EventLog* | *{*&#8202;Yes/True#8202;*\|*&#8202;No/False#8202;*}* Default is No. Log control actions to Eventlog. |
| *(28) InhibitTime* | Hours (integer) to inhibit Discharging after going into Charge mode. Default is 5. |
| *(29) Tup* | Duration, hrs, of upramp part for SCHEDULE mode. Default is 0.25. |
| *(30) TFlat* | Duration, hrs, of flat part for SCHEDULE mode. Default is 2.0. |
| *(31) Tdn* | Duration, hrs, of downramp part for SCHEDULE mode. Default is 0.25. |
|  *(32) kWThreshold* | Threshold, kW, for Follow mode. kW has to be above this value for the Storage element to be dispatched on. Defaults to 75% of the kWTarget value. Must reset this property after setting kWTarget if you want a different value. |
| &nbsp; *(33) DispFactor* | Defaults to 1 (disabled). Set to any value between 0 and 1 to enable this parameter. Use this parameter to reduce the amount of power requested by the controller in each control iteration. It can be useful when maximum control iterations are exceeded due to numerical in- stability such as fleet being set to charging and idling in subsequent control iterations (check the Eventlog). |
| &nbsp; *(34) ResetLevel* | The level of charge required for allowing the storage to discharge again after reaching the reserve storage level. After reaching this level, the storage control will not allow the storage device to discharge, forcing the storage to charge. Once the storage reaches thislevel, the storage will be able to discharge again. This value is a number between 0.2 and 1. |
| &nbsp; *(35) Seasons* | With this property the user can specify the number of targets to be used by the controller using the list given at “SeasonTar- gets”/“SeasonTargetsLow”, which can be used to dynamically adjust the storage controller during a QSTS simulation. The default value is 1. This property needs to be defined before defining SeasonTarget- s/SeasonTargetsLow. |


| &nbsp; *(36) SeasonTargets* | An array of doubles specifying the targets to be used during a QSTS simulation. These targets will take effect only if SeasonRating=true. The number of targets cannot exceed the number of seasons defined at the SeasonSignal.The difference between the targets defined at Sea- sonTargets and SeasonTargetsLow is that SeasonTargets applies to dis- charging modes, while SeasonTargetsLow applies to charging modes. |
| --- | --- |
| &nbsp; *(37) SeasonTargetsLow* | An array of doubles specifying the targets to be used during a QSTS simulation. These targets will take effect only if SeasonRating=true. The number of targets cannot exceed the number of seasons defined at the SeasonSignal.The difference between the targets defined at Sea- sonTargets and SeasonTargetsLow is that SeasonTargets applies to dis- charging modes, while SeasonTargetsLow applies to charging modes. |



***
_Created with the Standard Edition of HelpNDoc: [Create iPhone web-based documentation](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
