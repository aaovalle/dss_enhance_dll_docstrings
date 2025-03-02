# TIndMach012Obj

| ***TIndMach012Obj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description – (Specific class) otherwise generic* |
| **Implements the following properties/methods as in TLoadObj:** **RecalcElementData** **CalcYPrim** **MakePosSequence** **InjCurrents** **GetInjCurrents** **GetCurrents** **InitPropertyValues** **DumpProperties** **CalcDailyMult** **CalcDutyMult** **CalcYearlyMult** **GetPropertyValue** **CalcYPrimMatrix** **CalcInjCurrentArray** **GetTerminalCurrents** **DoHarmonicMode** **InitHarmonics** |  |  |
| **Method- private** | InterpretOption | Interprets the option for slip option. |
| **Method - private** | set\_Localslip | Sets the slip locally using the slip option set by the user. |
| **Method - private** | Get\_PFlowModelCurrent | Gets the power flow model current. |
| **Method - private** | Get\_DynamicModelCurrent | Uploads the injection currents for dynamics simulation mode. |
| **Method - private** | Set\_Slip | Sets the motor slip value. |
| **Property - private** | GetRotorLosses | Returns the rotor losses. |
| **Property - private** | GetStatorLosses | Returns the stator losses. |
| **Property - private** | Compute\_dSdP | Calculates and returns the dSdP based on rated slip and rated voltage. |
| **Method - private** | Randomize | Implements the typical process for handling randomization in DSS fashion. |
| **Method - private** | InitModel | Implements the routine for initializing the state variables and local variables of the model. |
| **Method - private** | CalcIndMach012ModelContribution | Calculates the current injections for the model. |
| **Method - private** | DoIndMach012Model | Computes the total terminal current for the model. |
| **Method - private** | CalcModel | Given the present voltages returns currents in accordance to the simulation mode. |
| **Method - private** | InitTraceFile | Initializes file for debugging purposes. |
| **Method - private** | WriteTraceRecord | Adds a new line to the trace file. |
| **Property - private** | Get\_PresentkV | Gets the present voltage base at the model terminals. |
| **Method - private** | Set\_PresentkV | Sets the present voltage base at the model terminals. |
| **Method - private** | SetPowerkW | Sets the kW base for the model. |
| **Method - protected** | Set\_ConductorClosed | Overrides the more generic class implementation to open/close model’s conductors. |
| **Method - protected** | DoDynamicMode | Implements the routine for calculating the injection currents for the model in dynamics simulation mode. |
| **Method - public** | Integrate | Implements the procedure for integrating the state variables of the model in dynamics simulation mode. |
| **Method - public** | CalcDynamic | Provides the structure for calculating the dynamic injection currents for the model. |
| **Method - public** | CalcPFlow | Calculates the power flow for the model using the local symmetric components. |
| **Method - public** | SetNominalPower | Sets the power output for the model. |
| **Property - public** | NumVariables | Overrides the more generic class implementation, returns the number of state variables in this model. |
| **Method - public** | GetAllVariables | Overrides the more generic class implementation, uploads the values for the state variables in this model into the given pointer. |
| **Property - public** | Get\_Variable | Overrides the more generic class implementation, returns the value for the state variable pointed by given index. |
| **Method - public** | Set\_Variable | Overrides the more generic class implementation, sets the value for the state variable pointed by given index. |
| **Property - public** | VariableName | Overrides the more generic class implementation, returns name of the state variable pointed by given index. |
| **Method - public** | InitStateVars | Overrides the more generic class implementation, initializes the state variables. |
| **Method - public** | IntegrateStates | Overrides the more generic class implementation, solves, and integrates the differential equation describing the model dynamics. |
| **Property - public** | LocalSlip | PA S\! (variable) and set\_Localslip. |
| **Property - public** | Slip | PA Set\_Slip. |
| **Property - public** | PresentkV | PA Get\_PresentkV and Set\_PresentkV. |



***
_Created with the Standard Edition of HelpNDoc: [Ensure High-Quality Documentation with HelpNDoc's Hyperlink and Library Item Reports](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
