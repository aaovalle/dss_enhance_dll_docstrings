# TStorageObj

| ***TStorageObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description – (Specific class) otherwise generic* |
| **Implements the following properties/methods as in TLoadObj, *TIndMach012Obj, TPVSystemObj and TGeneratorObj*:** **RecalcElementData** **CalcYPrim** **MakePosSequence** **InjCurrents** **GetInjCurrents** **GetCurrents** **InitPropertyValues** **DumpProperties** **CalcDailyMult** **CalcDutyMult** **CalcYearlyMult** **GetPropertyValue** **CalcYPrimMatrix** **CalcInjCurrentArray** **GetTerminalCurrents** **DoHarmonicMode** **InitHarmonics** **Integrate** **StickCurrInTerminalArray** **WriteTraceRecord** **Set\_ConductorClosed** **VariableName** **NumVariables** **GetAllVariables** **Get\_Variable** **Set\_Variable** **VariableName** **Randomize** **InitStateVars** **IntegrateStates** **CalcVTerminalPhase** **DoDynamicMode** **DoUserModel** **SetDragHandRegister** **Get\_PresentkW** **Get\_Presentkvar** **Get\_PresentkV** **Set\_PresentkV** **Set\_Presentkvar** **Set\_PresentkW** **Set\_PowerFactor** **ComputeInverterPower** **ComputekWkvar** **Set\_pf\_wp\_nominal** **Get\_Varmode** **Set\_Varmode** **Get\_VWmode** **Set\_VVmode** **Get\_VVmode** **Set\_DRCmode** **Get\_DRCmode** **Set\_AVRmode** **Get\_AVRmode** **Set\_VWmode** **kWOut\_Calc** **Get\_WPmode** **Set\_WPmode** **Get\_WVmode** **Set\_WVmode** **Get\_InverterON** **Set\_InverterON** **Get\_VarFollowInverter** **Set\_VarFollowInverter** **Set\_Maxkvar** **Set\_Maxkvarneg** **ResetRegisters** **TakeSample** |  |  |
| **Method- private** | ComputePresentkW | Calculates the present power output considering the model features. |
| **Method- private** | ComputeDCkW | Computes actual DC power (kW) to Update Storage State of Charge (SoC). |
| **Method- private** | CalcStorageModelContribution | Calculates Storage element current and adds it properly into the injcurrent array routines may also compute ITerminal&nbsp; (ITerminalUpdated flag). |
| **Method- private** | DoConstantPQStorageObj | Compute total terminal current for Constant PQ model. |
| **Method- private** | DoConstantZStorageObj | Compute total terminal current for constant Z model. |
| **Method- private** | DoDynaModel | Implements the routine for doing the user written dynamics model. |
| **Method- private** | CheckStateTriggerLevel | This is where we set the state of the Storage element. |
| **Method- private** | UpdateStorage | Updates Storage elements based on present kW and IntervalHrs variable. |
| **Property- private** | NormalizeToTOD | Normalizes time to a floating-point number representing time of day If Hour \> 24, time should be 0 to 24. |
| **Property- private** | InterpretState | Interprets the present state of the storage device (charging, discharging, idle). |
| **Property- private** | DecodeState | Returns the name of the storage state (charging, discharging, idle) as string. |
| **Property- private** | Get\_kvarRequested | Returns the present kvar requested. |
| **Property- private** | Get\_kWRequested | Returns the present kW requested. |
| **Method- private** | Set\_kW | Sets the present kW rating. |
| **Property- private** | Get\_kW | Returns the present kW rating. |
| **Method- private** | Set\_kWRequested | Sets the present kW requested. |
| **Method- private** | Set\_kvarRequested | Sets the present kvar requested. |
| **Method- private** | Set\_StorageState | Sets the storage state using the given integer. |
| **Method- private** | Set\_pctkWOut | Sets the discharging efficiency for the storage. |
| **Method- private** | Set\_pctkWIn | Sets the charging efficiency for the storage. |
| **Property- private** | Get\_DCkW | Returns the DC power rating for the storage. |
| **Property- private** | Get\_kWTotalLosses | Returns total losses: Idling + inverter + interface losses. |
| **Property- private** | Get\_InverterLosses | Returns the inverter losses. |
| **Property- private** | Get\_kWIdlingLosses | Returns Idling losses. |
| **Property- private** | Get\_kWChDchLosses | Returns the DC/AC interface losses. |
| **Method- private** | Update\_EfficiencyFactor | Updates the efficiency factor in time. |
| **Method- private** | Set\_StateDesired | Sets the state for the storage device using the given integer. |
| **Property- private** | Get\_kWDesired | Returns the kW desired, normally set by a controller. |
| **Method- private** | Set\_pctkWrated | Sets the kW rating as percentage of the nominal kW. |
| **Property- private** | Get\_CutOutkWAC | Gets the cutout limit for the inverter generation threshold.&nbsp; |
| **Property- private** | Get\_CutInkWAC | Gets the cut in limit for the inverter charging threshold.&nbsp; |
| **Method-public** | SetNominalStorageOutput | Sets the power output for the storage according to its present features. |



***
_Created with the Standard Edition of HelpNDoc: [Powerful and User-Friendly Help Authoring Tool for Markdown Documents](<https://www.helpndoc.com/feature-tour/markdown-import-export-using-helpndoc-help-authoring-tool/>)_
