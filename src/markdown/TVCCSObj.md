# TVCCSObj

| ***TVCCSObj*** |  |  |  |  |
| --- | --- | --- | --- | --- |
| ***Type-access*** |  | *Command* | *Description – (Specific class) otherwise generic* |  |
| **Implements the following properties/methods as in TLoadObj, *TIndMach012Obj, TPVSystemObj and TGeneratorOb*:** **RecalcElementData** **CalcYPrim** **MakePosSequence** **InjCurrents** **GetInjCurrents** **GetCurrents** **InitPropertyValues** **DumpProperties** **Get\_Variable** **Set\_Variable** **GetPropertyValue** **NumVariables** **GetAllVariables** **VariableName** **InitStateVars** **IntegrateStates** |  |  |  |  |
| **Method- private** | InitPhasorStates |  |  | Initializes the history terms for HW model source convention. |
| **Method- private** | IntegratePhasorStates |  |  | Integrates the phasor states for the next simulation iteration. |
| **Method- private** | ShutoffInjections |  |  | Support for DYNAMICMODE, NB: in phasor mode, use load convention for OpenDSS-X, stops injecting if the terminal opens. |
| **Method- private** | UpdateSequenceVoltage |  |  | Updates the register containing the sequence voltages at the terminal. |



***
_Created with the Standard Edition of HelpNDoc: [What is a Help Authoring tool?](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
