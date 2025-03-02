# Reactive Power Dispatch

The reactive power of Storage element is similar to the PVSystem element. As shown in [Table 1](<DispatchModes.md#\_bookmark13>), the Storage element has two self-dispatch modes for reactive power: constant power factor (PF) and constant reactive power (kvar). The modes can be activated by simply assigning a value to the Storage element *pf* or *kvar* properties.

In constant PF mode, the reactive power is calculated directly from the actual active power being dispatched. By default, the Storage element operates in constant PF mode with unity power factor. A positive power factor means reactive power flowing in the same direction as the active power, whereas a negative power factor means reactive and active powers flowing in opposite directions. Hence, depending on the Storage element operating state, the constant PF mode can cause the Storage element to either generate or absorb reactive power .

In constant kvar mode, the reactive power requested through *kvar* is decoupled from the active power. The sign convention is the same as for active power, i.e., a positive *kvar* means power flowing out of the element (var generation) and a negative *kvar* means power flowing into the element (var absorption).

Note that the active and reactive powers are subject to the inverter capability curve and other limiting functions. Thus, the actual powers at the Storage grid interface may differ from the requested ones. For more information, see \[[3](<References1.md#\_bookmark36>)\] and \[[5](<References1.md#\_bookmark38>)\].


***
_Created with the Standard Edition of HelpNDoc: [Modernize your help files with HelpNDoc's WinHelp HLP to CHM conversion tool](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
