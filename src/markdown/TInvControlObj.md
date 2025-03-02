# TInvControlObj

| ***TInvControlObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Implements the following properties/methods as in TCapControlObj and TExpControlObj:** **RecalcElementData** **CalcYPrim** **GetLosses** **GetPropertyValue** **InitPropertyValues** **DumpProperties** **SaveWrite** **MakePosSequence** **Sample** **DoPendingAction** **Reset** **Set\_PendingChange** **Get\_PendingChange** **GetCurrents** **GetInjCurrents** |  |  |
| **Property-private** | InterpretAvgVWindowLen | Interprets and assigns the Volt-watt control window length for the controller operation. |
| **Property-private** | InterpretDRCAvgVWindowLen | Interprets and assigns the DRC control window length for the controller operation. |
| **Property-private** | ReturnElementsList | Returns the list of controlled elements as string. |
| **Method-private** | UpdateInvControl | Updates the inv controls state by adding the present power flow solution voltage to the rolling average window. |
| **Method-private** | UpdateDERParameters | Updates the controlled devices according to the controller state. |
| **Method-private** | CalcVoltWatt\_watts | Calculates power output in VW mode. |
| **Method-private** | CalcQVVcurve\_desiredpu | Calculates reactive power output in VV mode. |
| **Method-private** | CalcQWPcurve\_desiredpu | Calculates reactive power output in WP mode. |
| **Method-private** | CalcQWVcurve\_desiredpu | Calculates reactive power output in WV mode. |
| **Method-private** | CalcQDRC\_desiredpu | Calculates reactive power output in DRC mode. |
| **Method-private** | CalcQAVR\_desiredpu | Calculates reactive power output in AVR mode. |
| **Method-private** | Check\_Qlimits | Checks if the present values are within allowed limits. |
| **Method-private** | Check\_Qlimits\_WV | Checks if the present values are within allowed limits (WV mode). |
| **Method-private** | Calc\_PQ\_WV | Calculates active and reactive powers in WV mode. |
| **Method-private** | Calc\_QHeadRoom | Calculates the present headroom for reactive power. |
| **Method-private** | CalcVoltVar\_vars | Calculates the reactive power for VV mode. |
| **Method-private** | CalcAVR\_vars | Calculates the reactive power for AVR mode. |
| **Method-private** | CalcWATTPF\_vars | Calculates the reactive power for WATTPF mode. |
| **Method-private** | CalcWATTVAR\_vars | Calculates the reactive power for WATTVAR mode. |
| **Method-private** | CalcDRC\_vars | Calculates the reactive power for DRC mode. |
| **Method-private** | CalcVVDRC\_vars | Calculates the reactive power for VVDRC mode. |
| **Method-private** | CalcLPF | Applies the LPF: Returns value is in kvar for VARS. Return value is in puPmpp for WATTS. |
| **Method-private** | CalcRF | Applies the Rise/Fall limiting function. |
| **Method-private** | Calc\_PBase | Calculates the active power base. |
| **Method-private** | Check\_Plimits | Calculates power limits. |
| **Method-private** | CalcPVWcurve\_limitpu | Calculates PVW curve limits in pu. |
| **Method-private** | GetmonVoltage | Gets the voltage at the point of connection of the DER. |
| **Method-private** | Change\_deltaQ\_factor | Updates delta Q factor. |
| **Method-private** | Change\_deltaP\_factor | Updates delta P factor. |
| **Property-public** | MakeDERList | Allocates memory for storing the list of DER to be controlled by this controller. |
| **Property-public** | PendingChange | PA Get\_PendingChange and Set\_PendingChange. |
| **Property-public** | Mode | PA ControlMode (variable). |
| **Property-public** | CombiMode | PA CombiControlMode (variable). |
| **Property-public** | DERNameList | PA FDERNameList (variable). |
| **Property-public** | vvc\_curve1 | PA Fvvc\_curvename (variable). |
| **Property-public** | hysteresis\_offset | PA Fvvc\_curveOffset (variable). |
| **Property-public** | voltage\_curvex\_ref | PA FVoltage\_CurveX\_ref (variable). |
| **Property-public** | avgwindowlen | PA FRollAvgWindowLength (variable). |
| **Property-public** | voltwatt\_curve | PA Fvoltwatt\_curvename (variable). |
| **Property-public** | voltwattCH\_curve | PA FvoltwattCH\_curvename (variable). |
| **Property-public** | DbVMin | PA FDbVMin (variable). |
| **Property-public** | DbVMax | PA FDbVMax (variable). |
| **Property-public** | ArGraLowV | PA FArGraLowV (variable). |
| **Property-public** | DynReacavgwindowlen | PA FDRCRollAvgWindowLength (variable). |
| **Property-public** | DeltaQ\_factor | PA FDeltaQ\_factor (variable). |
| **Property-public** | VoltageChangeTolerance | PA FVoltageChangeTolerance (variable). |
| **Property-public** | VarChangeTolerance | PA FVarChangeTolerance (variable). |
| **Property-public** | VoltwattYAxis | PA FVoltwattYAxis (variable). |
| **Property-public** | LPFTau | PA FLPFTau (variable). |
| **Property-public** | RiseFallLimit | PA FRiseFallLimit (variable). |
| **Property-public** | DeltaP\_factor | PA FDeltaP\_factor (variable). |
| **Property-public** | RefReactivePower | PA FReacPower\_ref (variable). |
| **Property-public** | ActivePChangeTolerance | PA FActivePChangeTolerance (variable). |
| **Property-public** | monVoltageCalc | PA FMonBusesPhase (variable). |
| **Property-public** | monBus | PA FMonBusesNameList (variable). |
| **Property-public** | monBusVbase | PA FMonBusesVbase (variable). |
| **Property-public** | v\_setpoint | PA Fv\_setpoint (variable). |



***
_Created with the Standard Edition of HelpNDoc: [Free CHM Help documentation generator](<https://www.helpndoc.com>)_
