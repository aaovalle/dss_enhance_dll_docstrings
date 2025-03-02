# Dispatch Modes

&nbsp;

The Storage element has several different dispatch modes, i.e., different ways to control the operation of a Storage element. The dispatch modes can be divided into self-dispatch modes and other dispatch modes. In self-dispatch modes, a Storage element determines its own operation. In the other dispatch modes, the storage operation is determined by a combination of StorageController and InvControl control elements. The currently available Storage element dispatch modes are summarized in [Table 1](<DispatchModes.md#\_bookmark13>).

The dispatch modes can be further divided into active and reactive power dispatch modes. Separate dispatch modes can be used for active power and reactive power but it is not possible to simultaneously use multiple dispatch modes for active power or reactive power. It is however, possible to use separate charging-specific and discharging-specific active power dispatch modes. For instance, the following combinations are allowed:

* Active power and reactive power dispatch driven by Follow self-dispatch mode and InvControl’s Volt-Var function, respectively;
* Active power and reactive power dispatch driven by StorageController‘s Time mode and In- vControl’s Volt-Var function, respectively;
* Active power and reactive power dispatch driven by StorageController‘s PeakShave (for charg- ing) and PeakShaveLow (for discharging) modes and InvControl’s Volt-Var function, respectively;

It is worth mentioning that InvControl‘s VW function can always be applied simultaneously with any other active power dispatch mode, because it has a “limiting nature”, differently from the modes presented in [Table 1](<DispatchModes.md#\_bookmark13>), which have a “requesting nature”.

Table 1: Currently Available Storage Element Dispatch Modes

| **Measure** | **Means** | **Mode/Function** |
| --- | --- | :---: |
| &nbsp; &nbsp; &nbsp; Active Power |  &nbsp; Self-Dispatch | Default |
|  |  | Follow |
|  |  | LoadLevel |
|  |  | Price |
|  |  | External |
|  |  | TimeChargeTrigger (Discharge Only) |
|  |  &nbsp; StorageController | PeakShave (Discharge Only) |
|  |  | Follow (Discharge Only) |
|  |  | Support (Discharge Only) |
|  |  | Loadshape |
|  |  | PeakShaveLow (Charge Only) |
|  |  | Time |
|  |  | Schedule (Discharge Only) |
| &nbsp; Reactive Power | Self-Dispatch | Constant PF |
|  |  | Constant kvar |
|  |  InvControl | Volt-Var (VV) |
|  |  | Dynamic Reactive Current (DRC) |
|  |  | VV + DRC |
|  |  | VV + Volt-Watt (VW) |


&nbsp;

**Note:** As specified in IEEE1547-2018\[[4](<References1.md#\_bookmark37>)\], the smart-inverter Volt-Watt function applied to energy storage systems may require the element to charge during high voltage scenarios. Thus, the InvControl element could also be added as a mean to control the active power dispatch of a storage element under VW function. However, this functionality has not been implemented yet. Currently, the curve specified for VW function can only limit the active power dispatch to a value as low as zero.

This technical note focuses on the self-dispatch modes, for both active and reactive powers. For more information on the modes/functions available in StorageController and InvControl elements, see \[[2](<References1.md#\_bookmark35>)\] and \[[3](<References1.md#\_bookmark36>)\].

Three of the five active power self-dispatch modes: Default, LoadLevel and Price, are commanded by two triggers: one for charging, named *ChargeTrigger*, and the other for discharging, *DischargeTrigger*. In general, a Storage element operates in a given state until one of the following events happens:

* The stored energy, *kWhstored*, reaches the element’s rated capacity *kWhRated* when in charg- ing state. In this case, the element automatically goes to idling state;
* The stored energy reaches its minimum reserve, %*reserve*, when in discharging state. In this case, the element automatically goes to idling state;
* A trigger is activated. In this case, the storage automatically goes to the state determined by the respective trigger, i.e., if *ChargeTrigger* has been activated, the storage goes to charging state, whereas if the *DischargeTrigger* has been activated, the storage goes to discharging state;
* The user manually sets a new state: this can be done either through the parameter *state* or *kW* ;
* The storage receives a request from a StorageController element to operate in a specific state;

For the last three cases above, the element only operates in the selected/requested state if there is enough energy stored/left. In other words, a given state and charge/discharge rate can always be requested from a storage element but the storage operation may be limited among other things by the storage energy capacity and the storage inverter operating limits (the inverter capability curve or limit active power output and VW functions). The following subsections introduce the self-dispatch modes.


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Convert Your Word Doc to an eBook: A Step-by-Step Guide](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
