# TGeneratorObj

| ***TGeneratorObj*** |  |  |  |
| --- | --- | --- | --- |
| ***Type-access*** | *Command* |  | *Description – (Specific class) otherwise generic* |
| **Implements the following properties/methods as in TLoadObj and *TIndMach012Obj*:** **RecalcElementData** **CalcYPrim** **MakePosSequence** **InjCurrents** **GetInjCurrents** **GetCurrents** **InitPropertyValues** **DumpProperties** **CalcDailyMult** **CalcDutyMult** **CalcYearlyMult** **GetPropertyValue** **CalcYPrimMatrix** **CalcInjCurrentArray** **GetTerminalCurrents** **DoHarmonicMode** **InitHarmonics** **Integrate** **StickCurrInTerminalArray** **WriteTraceRecord** **Set\_ConductorClosed** **VariableName** **NumVariables** **GetAllVariables** **Get\_Variable** **Set\_Variable** **VariableName** **Randomize** **InitStateVars** **IntegrateStates** **CalcVTerminalPhase** |  |  |  |
| **Method- private** | CalcGenModelContribution | Calculates the injection currents for the element based on the model type. |  |
| **Method- private** | CalcVterminal | Calculates and uploads the voltage at the element’s terminals using the model and connection type as reference. |  |
| **Method- private** | CalcVthev\_Dyn | Calculates the Thevenin voltage equivalent for dynamics simulation. |  |
| **Method- private** | DoConstantPQGen | Implements the routine for calculating the injection currents for generator model when working in constant PQ mode. |  |
| **Method- private** | DoConstantZGen | Implements the routine for calculating the injection currents for generator model when working as constant admittance. |  |
| **Method- private** | DoCurrentLimitedPQ | Implements the routine for calculating the injection currents for generator model when working as constant kW, kvar, but current-limited below Vminpu. Approximates a simple inverter. |  |
| **Method- private** | DoDynamicMode | Implements the routine for calculating the injection currents for generator model when working in dynamics simulation mode. |  |
| **Method- private** | DoFixedQGen | Implements the routine for calculating the injection currents for generator model when working as constant kW, fixed Q. |  |
| **Method- private** | DoFixedQZGen | Implements the routine for calculating the injection currents for generator model when working as constant kW, fixed Q (as a constant reactance). |  |
| **Method- private** | DoPVTypeGen | Implements the routine for calculating the injection currents for generator model when working as constant kW, constant kV.&nbsp; Somewhat like a conventional transmission power flow P-V generator. |  |
| **Method- private** | DoUserModel | Implements the routine for calculating the injection currents for a user generator model (DLL). |  |
| **Property- private** | CheckOnFuel | Returns a boolean flag indicating if the fuel tank (if any) is empty. |  |
| **Method- private** | SetDragHandRegister | Moves the internal shift register according to the given value. |  |
| **Method- private** | SyncUpPowerQuantities | Keeps kvar nominal up to date with kW and PF. |  |
| **Property- private** | Get\_PresentkW | Returns the present kW delivered by the model. |  |
| **Property- private** | Get\_Presentkvar | Returns the present kvar delivered/absorbed by the model. |  |
| **Property- private** | Get\_PresentkV | Returns the present kV at the terminals of the model. Considers the connection mode (wye/delta). |  |
| **Method- private** | Set\_PresentkV | Sets the present kV at the terminals of the model. Considers the connection mode (wye/delta). |  |
| **Method- private** | Set\_Presentkvar | Sets the present kvar delivered/absorbed by the model. |  |
| **Method- private** | Set\_PresentkW | Sets the present kW delivered by the model.&nbsp; |  |
| **Method- private** | Set\_PowerFactor | Sets the present power factor delivered by the model.&nbsp; |  |
| **Method- private** | SetkWkvar | Sets the present kW and kvar for the model. |  |
| **Method- public** | SetNominalGeneration | Implements the calls for calculating the injection currents for the model considering its features. |  |
| **Method- public** | ResetRegisters | Resets all the registers needed for integration and the local energy meter. |  |
| **Method- public** | TakeSample | Commands the local energy meter to take a sample. |  |
| **Method- public** | InitDQDVCalc | Initializes DQ DV registers. |  |
| **Method- public** | BumpUpQ | Bump up vars by 10% of range for next calculation. |  |
| **Method- public** | RememberQV | Stores Q and V for further use. |  |
| **Method- public** | CalcDQDV | Calculates DQ and DV. |  |
| **Method- public** | ResetStartPoint | Resets the Q nominal per phase to the initial (default) value. |  |
| **Property- public** | CheckIfDynVar | Evaluates if the value provided corresponds to a constant value or to an operand for calculating the value using the simulation results, this is useful when a DynamicExp is linked to the generator. |  |
| **Method- public** | SetDynOutput | Obtains the indexes of the given variables to use them as reference for setting the dynamic output for the generator when using DynamicExp with the generator. |  |
| **Property- public** | PresentkW | PA Get\_PresentkW and Set\_PresentkW. |  |
| **Property- public** | Presentkvar | PA Get\_Presentkvar and Set\_Presentkvar. |  |
| **Property- public** | ForcedON | PA FForcedON (variable). |  |
| **Property- public** | PresentkV | PA Get\_PresentkV and Set\_PresentkV. |  |
| **Property- public** | PowerFactor | PA PFNominal (variable) and Set\_PowerFactor. |  |



***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Capabilities with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
