# TRegControlObj

| ***TRegControlObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Implements the following properties/methods as in TCapControlObj and TExpControlObj:** **RecalcElementData** **CalcYPrim** **GetLosses** **GetPropertyValue** **InitPropertyValues** **DumpProperties** **SaveWrite** **MakePosSequence** **Sample** **DoPendingAction** **Reset** **Set\_PendingChange** **Get\_PendingChange** **GetCurrents** **GetInjCurrents** |  |  |
| **Property-private** | Get\_Transformer | Returns a pointer to the controlled transformer. |
| **Property-private** | Get\_Winding | Returns the index of the active winding. |
| **Property-private** | Get\_MinTap | Returns the minimum tap value. |
| **Property-private** | Get\_MaxTap | Returns the maximum tap value. |
| **Property-private** | Get\_TapIncrement | Returns the tap increment value. |
| **Property-private** | Get\_NumTaps | Returns the number of taps for the active winding. |
| **Property-private** | Get\_TapNum | Returns the present tap number. |
| **Method-private** | RegWriteTraceRecord | Adds a new line to the trace record using the present values. |
| **Method-private** | RegWriteDebugRecord | Adds a new line to the debug record using the present values. |
| **Method-private** | set\_PendingTapChange | Sets the flags indicating that there is a tap change pending for being applied. |
| **Method-private** | AtLeastOneTap | Called in STATIC mode. Changes 70% of the way but at least one tap, subject to maximum allowable tap change. |
| **Property-private** | ComputeTimeDelay | Computes time delay for the next tap change (if any). |
| **Property-private** | GetControlVoltage | Gets the control voltage according to the controller’s configuration. |
| **Property-private** | Set\_TapNum | Sets the present tap for the active winding. |
| **Method-public** | SaveWrite | Overrides standard SaveWrite. Regcontrol structure not conducive to standard means of saving. |
| **Property-public** | Transformer | PA Get\_Transformer. |
| **Property-public** | TrWinding | pA Get\_Winding. |
| **Property-public** | PendingTapChange | pA FPendingTapChange (variable) and set\_PendingTapChange. |



***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create Professional Documentation with HelpNDoc's Clean UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
