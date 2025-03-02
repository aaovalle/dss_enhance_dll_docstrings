# TDynamicExpObj

| ***TDynamicExpObj*** |  |  |  |  |
| --- | --- | --- | --- | --- |
| ***Type-access*** |  | *Command* | *Description* |  |
| **Implements the following properties/methods as in TLoadShapeObj and TLineObj:** **InitPropertyValues**&nbsp; **DumpProperties** **GetPropertyValue** |  |  |  |  |
| **Property-private** | InterpretDiffEq |  |  | Builds the list of commands required for operating the equation declared, this &nbsp; automation is intended to accelerate the calculation in run time. |
| **Property-private** | Get\_Closer\_Op |  |  | Returns the index of the closest operator found in the given string starting from left to right. |
| **Property-private** | Get\_Var\_Idx |  |  | Returns the index of the variable if it exists in the state variable list, otherwise, it returns 50001 if the string entered is a numeric constant (DBL) or -1 if the string entered is neither a numeric constant nor state variable. |
| **Property-private** | Check\_If\_CalcValue |  |  | Checks if the given string is a value calculated by the element using the eq model. |
| **Property-private** | Get\_Out\_Idx |  |  | Gets the index for the given variable if it is an output. |
| **Property-private** | SolveEq |  |  | Implements the solver for the local equation. |
| **Property-private** | IsInitVal |  |  | Returns true if the given code is for an initialization value. |
| **Property-private** | Get\_DynamicEqVal |  |  | Returns the value of the state variable using the given indexes. |
| **Property-private** | Get\_VarName |  |  | Returns the name of the state variable corresponding to the given index. |
| **Property-private** | NumVars |  |  | PA FNumVars (variable). |



***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
