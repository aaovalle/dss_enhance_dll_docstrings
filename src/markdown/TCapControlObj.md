# TCapControlObj

| ***TCapControlObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Implements the following properties/methods as in TLineObj:** **RecalcElementData** **CalcYPrim** **GetLosses** **GetPropertyValue** **InitPropertyValues** **DumpProperties** **SaveWrite** **MakePosSequence** |  |  |
| **Property-private** | Get\_Capacitor | Returns the pointer to the controlled capacitor. |
| **Property-private** | NormalizeToTOD | Normalize time to a floating-point number representing time of day if Hour \> 24. Resulting time should be 0:00+ to 24:00 inclusive. |
| **Method-private** | Set\_PendingChange | Sets the flag for indicating that there is a pending change to be performed. |
| **Property-private** | Get\_PendingChange | Returns the value of the flag indicating if there is a pending change. |
| **Method-private** | GetControlVoltage | Gets the Voltage used for voltage control based on specified options. |
| **Method-private** | GetControlCurrent | Gets the current to control on based on type of control specified. |
| **Method-private** | GetBusVoltages | Gets the voltages at the bus specified. |
| **Method-public** | Sample | Samples control quantities and set action times in Control Queue. |
| **Method-public** | DoPendingAction | Do the action that is pending from last sample. |
| **Method-public** | Reset | Resets the controller to the initial defined state. |
| **Property-public** | This\_Capacitor | PA Get\_Capacitor. |
| **Property-public** | PendingChange | PA Get\_PendingChange and Set\_PendingChange. |



***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
