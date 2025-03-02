# Dispatch Modes

There are currently 7 discharge modes and 4 charging modes available, from which two modes, Loadshape and Time, can be used to manage both discharging and charging of the fleet. The controller can operate simultaneously with any combination of a discharge only and a charge only mode. Each mode can be further divided as “powerflow-driven” or “time-driven”. [Table 1](<DispatchModes1.md#\_bookmark1>) summarizes all dispatch modes available and their classification.

A “power flow-driven” mode has its operation based on an electrical measure resulting from a power flow solution, like in Figure 1. The measured quantity (power or current) is compared to a target, and the controller requests each element of the fleet to dispatch based on the difference between the measurement and the target values.

&nbsp;

All “power flow-driven” modes employ a deadband controller concept. A target value is set (*kWTarget*, *kWTargetLow*) and a band around the target is specified. When the kW in the monitored branch exceeds the *kWTarget* value plus half the bandwidth, the fleet is dispatched to bring the power back to the center of the band. The dispatch follows the regulated measure until the storage dispatch re- quested to a specific storage element wants to go negative, at which point it is set to idling state. The bandwidth is set either as a percentage of the respective target values through properties %*kWBand* and %*kWBandLow* (defaults to 2%) or as absolute values, through *kWBand* and *kWBandLow* properties.

Each Storage element may have a different weight, if you want the StorageController to dispatch some elements at a higher rate than others. The weights default to 1.0, but may be defined by an array.

A “time-driven” mode has its operation directly or indirectly based on time. The deadband concept does not apply to these modes. The dispatch rate is pre-defined based on either a dispatch curve or a fixed rate (%*RatekW* and %*RateCharge* properties).

Table 1: Summary of dispatch modes for StorageController element

| **Requested State** | **Driver** | **Mode** |
| :---: | :---: | :---: |
|  Discharging Only |  Power Flow | PeakShave |
|  |  | I-PeakShave |
|  |  | Follow |
|  |  | Support |
|  | Time | Schedule |
| Charging Only | Power Flow | PeakShaveLow |
|  |  | I-PeakShaveLow |
| Both | Time | Time |
|  |  | LoadShape |



***
_Created with the Standard Edition of HelpNDoc: [Make Help Documentation a Breeze with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
