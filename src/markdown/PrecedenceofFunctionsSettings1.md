# Precedence of Functions/Settings

As one may have noticed, there are several types of control functions that can be applied to Storage and PVSystem elements in OpenDSS. Some of those operate on the same electrical measure, i.e., active, or reactive power. In these cases, depending on the nature of the control function, they may be allowed to operate simultaneously, or they might be mutually exclusive. In the first case, it is necessary to establish an order of precedence. The precedence rules applied in OpenDSS follows the summary of functional descriptions for smart inverters from \[[6](<References7.md#\_bookmark25>)\] and in IEEE 1547-2018 \[[1](<References7.md#\_bookmark20>)\] requirements, where applicable. They have been adapted to OpenDSS context and are summarized in Tables [1](<PrecedenceofFunctionsSettings1.md#\_bookmark8>) and [2](<PrecedenceofFunctionsSettings1.md#\_bookmark9>) for functions/settings that manage active and reactive power, respectively.

Table 1: Precedence of Watt Related Functions

&nbsp;

| **Priority** | **Settings**/ **Functions** | **Description** |
| --- | --- | --- |
| &#49;st: Fundamental Physical Limit |  DER Primary Source of Energy | A DER cannot produce/absorb active power that it does not have avail- able. These represent the ultimate limit of the DER. For PVSystem, it is represented by the available active power at a given time instant and for Storage it is represented by the energy capacity available (depending on the relation between *kWhrated* and *kWhstored* for charging state and between %*stored* and %*reserve* for discharging state). |
| &#50;nd: Nameplate and Device Limits Settings |  Max Power Capability Setting | This is the configurable setting establishing the DER s maximum ac- tive power input/output: *kV A*, for PVSystem, and *kV A* and *kWRated*, for Storage. Higher or lower priority settings/functions may reduce the wattage output below this value, but nothing may increase it above this value. |
| &nbsp; 3rd: Settings Actively Affecting Operating Boundaries |  Limit DER Power Function | These functions serve to reduce maximum allowed watt level to some percentage of the Max Power Capability Setting less than 100%. The cause varies: For Volt-Watt function, it’s the voltage at the DER ter- minal (autonomous function). For Limit DER Power Output Function, it’s a direct control command (for instance, sent by the operator), spec- ified through property %*kWRated* for Storage and %*Pmpp* for PVSys- tem. They may be simultaneously active with the same relative priority. The one requiring the greatest reduction in watts takes precedence. As functions intended to establish operating boundaries, these functions are higher priority than any of the dynamic or steady-state functions. Those functions may be active at the same time as these functions but must operate (even dynamically) within the boundaries established by these functions. |
|  | &nbsp; Volt-Watt Function |  |
| &#52;th: Dynamic Functions | None at Current Version | These would be Dynamic Real-Power Support and Dynamic Volt-Watt functions. These are dynamic functions that would produce “additional” active power. See \[[6](<References7.md#\_bookmark25>)\] for more information. |
|  5th: Steady State Functions | Storage Direct Ch./Dch. | Each of these functions/dispatch modes serve to manage the flow of real power into or out of the DER. These functions are mutually exclusive and cannot be active simultaneously. The first one refers to the direct dispatch command through properties *kW* , *kvar*, *state*, %*charge*, and %*discharge*, whereas the second refers to any of the self-dispatch modes or any mode available through a StorageController CE. |
|  | Any Storage Dispatch Function |  |


&nbsp;

Table 2: Precedence of Vars Related Functions

&nbsp;

| **Priority** | **Settings**/ **Functions** | **Description** |
| --- | --- | --- |
| &#49;st: Fundamental Physical Limit |  Self-Imposed Limits |  None at current version |
| &#50;nd: Nameplate and Device Limits Settings |  Max Power Capability Setting | This is the configurable setting establishing the DER s maximum reactive power input/output: *kvarMax*, *kvarMaxAbs* and the ascending linear vars limit specified through %*PminNoV ars* and %*PminkvarMax* for both PVSystem and Storage. Higher or lower priority settings may re- duce the vars output/input below these values, but nothing may increase it above these values. |
| &#51;rd: Settings Actively Affecting Operating Boundaries | &nbsp; None defined for Vars |  &nbsp; None at current version |
| &#52;th: Dynamic Functions | DRC Function | This is a dynamic function and produces “Additional” reactive current that adds-to or subtracts-from whatever the present reactive current level may be based on one1 of the 5*th* priority functions. |
|  5th: Steady State Functions | Constant PF Function | These functions instruct the DER as to the desired level of reactive power to produce at any time. For each function, the reactive power level is indirectly related to the watt output. These functions have equal priority but are never in conflict because they are mutually exclusive and only one may be effective at any time. |
|  | Constant kvar Function |  |
|  | Volt-Var Function |  |


&nbsp;

&nbsp;

&#49;At current version, DRC can only be applied on top of Volt-Var function.


***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
