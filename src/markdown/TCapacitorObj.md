# TCapacitorObj

| ***TCapacitorObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Implements the following properties/methods as in TLineObj:** **RecalcElementData** **CalcYPrim** **GetLosses** **GetPropertyValue** **InitPropertyValues** **DumpProperties** **MakePosSequence** |  |  |
| **Property-private** | get\_States | Returns the present states for the capacitor bank. |
| **Method-private** | Set\_States | Sets the present states for the capacitor bank. |
| **Method-private** | set\_LastStepInService | Forces the last step in service to be a certain value. |
| **Method-private** | ProcessHarmonicSpec | Interprets and loads the assigned harmonic spectrum into the capacitor. |
| **Method-private** | ProcessStatesSpec | Interprets and loads the assigned states array for the cap bank. |
| **Method-private** | MakeYprimWork | Call this routine only if step is energized. |
| **Method-private** | set\_NumSteps | Sets the number of steps for the cap bank (1=kvar, 2=Cuf, 3=Cmatrix). |
| **Property-public** | AddStep | Connects the next capacitor from the bank. |
| **Property-public** | SubtractStep | Disconnects the next capacitor from the bank. |
| **Property-public** | AvailableSteps | Returns the number of available steps for connection. |
| **Method-public** | FindLastStepInService | Finds the last cap in service within the cap bank. |
| **Property-public** | NumSteps | PA FNumSteps (variable) and set\_NumSteps. |
| **Property-public** | States | PA get\_States and set\_States. |
| **Property-public** | Totalkvar | PA FTotalkvar (variable). |
| **Property-public** | NomKV | PA kvrating (variable). |
| **Property-public** | LastStepInService | PA FLastStepInService (variable) and set\_LastStepInService. |
| **Property-public** | NumTerminals | PA NumTerm (variable). |



***
_Created with the Standard Edition of HelpNDoc: [Easily create EBooks](<https://www.helpndoc.com/feature-tour>)_
