# TRelayObj

| ***TRelayObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Implements the following properties/methods as in TCapControlObj and TExpControlObj:** **RecalcElementData** **CalcYPrim** **GetLosses** **GetPropertyValue** **InitPropertyValues** **DumpProperties** **SaveWrite** **MakePosSequence** **Sample** **DoPendingAction** **Reset** **Set\_PendingChange** **Get\_PendingChange** **GetCurrents** **GetInjCurrents** |  |  |
| **Method-private** | InterpretRelayState | Interprets the relay state (open/closed/trip). |
| **Property-private** | get\_State | Returns the control state. |
| **Method-private** | set\_State | Sets the control state. |
| **Property-private** | get\_NormalState | Returns the control normal state. |
| **Method-private** | set\_NormalState | Sets the control normal state. |
| **Method-private** | InterpretRelayType | Interprets the relay type (current, voltage, etc.) |
| **Method-private** | OvercurrentLogic | Implements the overcurrent relay control logic. |
| **Method-private** | VoltageLogic | Implements the voltage relay control logic. |
| **Method-private** | RevPowerLogic | Implements the reverse power relay control logic. |
| **Method-private** | NegSeq46Logic | Implements the negative sequence 46 power relay control logic. |
| **Method-private** | NegSeq47Logic | Implements the negative sequence 47 power relay control logic. |
| **Method-private** | GenericLogic | Implements the generic relay control logic. |
| **Method-private** | DistanceLogic | Implements the distance relay control logic. |
| **Method-private** | TD21Logic | Implements the TD21 relay control logic. |
| **Method-private** | DirectionalOvercurrentLogic | Implements the directional overcurrent relay control logic. |
| **Property-public** | PresentState | PA get\_State and set\_State. |
| **Property-public** | NormalState | PA get\_NormalState and set\_NormalState. |



***
_Created with the Standard Edition of HelpNDoc: [Keep Your Sensitive PDFs Safe with These Easy Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
