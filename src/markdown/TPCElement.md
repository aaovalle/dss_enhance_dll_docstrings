# TPCElement

| ***TPCElement*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description – (Specific class) otherwise generic* |
| **Method- private** | GetTerminalCurrents | Returns the currents at the active terminal |
| **Property- private** | Get\_Variable | Returns the numeric value (double) of the state variable indicated in the argument by index. |
| **Method- private** | Set\_Variable | Sets the numeric value (double) of the state variable indicated in the argument by index. |
| **Method- public** | ZeroInjCurrent | Sets the local injection currents array to zero. |
| **Method- public** | InitPropertyValues | Initializes the local property array with the default values. |
| **Method- public** | GetCurrents | Gets the present current values at the active terminal. |
| **Method- public** | GetInjCurrents | Gets the injection currents array at the active terminal. |
| **Method- public** | ComputeIterminal | Overrides the generic class call to define the local procedure for computing the current at the element’s terminal. |
| **Property- public** | InjCurrents | Overrides the generic class call to define the local procedure for adding the local injection currents into System currents array. |
| **Method- public** | CalcYPrimContribution | Calculates the Yprim contribution to the injection currents array using the present values. |
| **Method- public** | DumpProperties | Implements the routine for writing the local properties down into a plain text file at the end. |
| **Method- public** | InitHarmonics | Initializes the variables of the calling object for harmonics simulation mode. |
| **Method- public** | set\_ITerminalUpdated | Sets the ITerminalUpdated flag using the value given in the argument. |
| **Method- public** | InitStateVars | Sets the foundation for initializing the state variables of the calling object. It is expected to be override by a more specific class. If not overridden, when called it does nothing. |
| **Method- public** | IntegrateStates | Sets the foundation for defining the procedure to integrate the state variables of the calling object. It is expected to be override by a more specific class. If not overridden, when called it does nothing. |
| **Property- public** | NumVariables | Sets the foundation for defining the number of state variables of the calling object. It is expected to be override by a more specific class. If not overridden, when called it does nothing. |
| **Method- public** | GetAllVariables | Sets the foundation for returning the values for all the state variables of the calling object. It is expected to be override by a more specific class. If not overridden, when called it does nothing. |
| **Property- public** | VariableName | Sets the foundation for returning the value the state variable indicated in the argument by index. It is expected to be override by a more specific class. If not overridden, when called it does nothing. |
| **Property- public** | LookupVariable | Search through variable name list and return index if found. Otherwise, returns -1. |
| **Property- public** | Property- public | PA Get\_Variable and Set\_Variable. |



***
_Created with the Standard Edition of HelpNDoc: [Easy EPub and documentation editor](<https://www.helpndoc.com>)_
