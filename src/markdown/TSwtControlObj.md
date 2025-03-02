# TSwtControlObj

| ***TSwtControlObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Implements the following properties/methods as in TCapControlObj, TRelayObj and TExpControlObj:** **RecalcElementData** **CalcYPrim** **GetLosses** **GetPropertyValue** **InitPropertyValues** **DumpProperties** **SaveWrite** **MakePosSequence** **Sample** **DoPendingAction** **Reset** **Set\_PendingChange** **Get\_PendingChange** **GetCurrents** **GetInjCurrents** **Set\_NormalState** |  |  |
| **Method-private** | InterpretSwitchAction | Interprets the switch action (open/closed/trip). |
| **Method-private** | set\_Flocked | Locks the switch control. |
| **Method-private** | Set\_LastAction | Sets the last pending action. |
| **Method-private** | Set\_PresentState | Changes the present state of the switch control. |
| **Property-public** | NormalState | PA FNormalState (variable) and Set\_NormalState. |
| **Property-public** | PresentState | PA FPresentState (variable) and Set\_PresentState. |
| **Property-public** | IsLocked | PA FLocked (variable). |
| **Property-public** | Locked | PA Flocked (variable) and set\_Flocked. |
| **Property-public** | CurrentAction | PA ActionCommand (variable) and Set\_LastAction. |



***
_Created with the Standard Edition of HelpNDoc: [Simplify Your Help Documentation Process with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
