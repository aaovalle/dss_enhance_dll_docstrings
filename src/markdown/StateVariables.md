# State Variables

[Table 2](<StateVariables.md#\_bookmark15>) lists all the state variables of the Storage element. The state variables can be monitored by setting a monitor for the Storage element in mode 3.

Table 2: State Variables of the Storage Element

| **State Variable** | **Description** |
| --- | --- |
| kWh | Stored Energy in kWh. |
| State | Storage state. 1 for discharging, -1 for charging and 0 for idling. |
| kWOut | Power flowing out of the element, in kW. It is a result from the power flow. For discharging state. |
| kWIn | Power flowing into the element in kW. It is a result from the power flow. For charging and idling states. |
| kvarOut | Power flowing out of the element in kvar as a signed-value. Positive for vars generation and negative for vars absorption. |
|  DCkW | DC power flowing into the storage inverter in kW at the DC side of the inverter as a signed-value. Positive for power flowing into the grid and negative for power flowing into the Storage element. |
| kWTotalLosses | Total losses in kW. |
| kWInvLosses | Inverter losses in kW. |
| kWIdlingLosses | Idling losses in kW. |
| kWChDchLosses | Charging and discharging losses in kW. |
|  kWh Chng | Energy variation from the last time step, in kWh. Corresponds to the power that effectively charges/discharges the storage medium/battery multiplied by the time step length. |
| InvEff | Inverter efficiency. |
| InverterON | Flag indicating the inverter status. See \[[3](<References1.md#\_bookmark36>)\]. |
| Vref | Reference voltage used by the voltage-dependent InvControl function- alities. Equal to 9999 if there is no InvControl controlling the Storage element. See \[[3](<References1.md#\_bookmark36>)\]. |


| Vavg (DRC) | Average voltage of the moving window used in InvControl’s DRC func- tion. Equal to 9999 if there is no InvControl controlling the element. See \[[3](<References1.md#\_bookmark36>)\]. |
| --- | --- |
|  VV Oper | Flag variable that indicates the status of InvControl’s Volt-Var function operation. Equal to 9999 if there is no InvControl controlling the element. See \[[3](<References1.md#\_bookmark36>)\]. |
|  VW Oper | Flag variable that indicates the status of InvControl’s Volt-Watt func- tion operation. Equal to 9999 if there is no InvControl controlling the element. See\[[3](<References1.md#\_bookmark36>)\]. |
|  DRC Oper | Flag variable that indicates the status of InvControl’s DRC function operation. Equal to 9999 if there is no InvControl controlling the element. See \[[3](<References1.md#\_bookmark36>)\]. |
|  VV DRC Oper | Flag variable that indicates the status of InvControl’s VV + DRC function operation. Equal to 9999 if there is no InvControl controlling the element. See \[[3](<References1.md#\_bookmark36>)\]. |
| kWDesired | Nominal power desired or requested by the dispatch mode selected, in kW, if there is enough energy capacity left. Otherwise, it is 0. |
| kW VW Limit | Active power limit imposed by Volt-Watt function, in kW. See \[[3](<References1.md#\_bookmark36>)\]. Equal to 9999 if the function is disabled due to inverter status. |
| Limit kWOut Function | Active power limit imposed by “Limit DER output function” (%*kWRated × kWRated*), in kW. See \[[3](<References1.md#\_bookmark36>)\]. |
| kVA Exceeded | Flag indicating if inverter kVA rating has been exceeded. See \[[3](<References1.md#\_bookmark36>)\]. |



***
_Created with the Standard Edition of HelpNDoc: [Transform Your Word Doc into a Professional-Quality eBook with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
