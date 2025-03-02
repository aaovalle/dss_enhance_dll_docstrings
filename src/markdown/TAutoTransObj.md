# TAutoTransObj

| ***TAutoTransObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Implements the following properties/methods as in TLineObj:** **RecalcElementData** **CalcYPrim** **GetLosses** **GetPropertyValue** **InitPropertyValues** **DumpProperties** **SaveWrite** **MakePosSequence** |  |  |
| **Property-private** | Get\_PresentTap | Returns the present tap for the active winding. |
| **Method-private** | Set\_PresentTap | Sets the present tap for the active winding. |
| **Property-private** | Get\_MinTap | Returns the minimum tap for the active winding. |
| **Property-private** | Get\_MaxTap | Returns the maximum tap for the active winding. |
| **Property-private** | Get\_TapIncrement | Returns the tap increment for the active winding. |
| **Property-private** | Get\_BaseVoltage | Returns the base voltage (LN) for the active winding. |
| **Property-private** | Get\_BasekVLL | Returns the base voltage (LL) for the active winding. |
| **Property-private** | Get\_NumTaps | Returns the number of taps for the active winding. |
| **Property-private** | Get\_WdgResistance | Returns the resistance for the active winding. |
| **Property-private** | Get\_WdgConnection | Returns the connection type for the active winding. |
| **Property-private** | Get\_WdgkVA | Returns the nominal kVA for the active winding. |
| **Property-private** | Get\_Xsc | Returns the reactance for the active winding. |
| **Property-private** | Get\_WdgYPPM | Returns the parts per million of transformer winding VA rating connected to ground to protect against accidentally floating a winding without a reference. Applies for the active winding. |
| **Method-private** | CalcY\_Terminal | Calculates the Y primitive at the active winding. |
| **Method-private** | GICBuildYTerminal | Calculates the Y primitive at the active winding at the given frequency. |
| **Method-private** | BuildYPrimComponent | Routine used to add every element of Y\_terminal into Yprim somewhere. |
| **Method-private** | FetchXfmrCode | Imports the features of the XfmrCode assigned into the active element. |
| **Property-private** | GeTAutoWindingCurrentsResult | Returns string mag, angle for the active winding. |
| **Method-private** | SetBusAuto | For winding 2 set all nodes on second end of winding to same as 1st value so all neutral ends of common winding get connected to same neutral node. |
| **Method-protected** | SetTermRef | Sets an array which maps the two conductors of each winding to the phase and neutral conductors of the AutoTrans according to the winding connection. |
| **Method-public** | SetNumWindings | Sets the number of windings for the element, creates the windings objects needed. |
| **Method-public** | SetNodeRef | Overrides the more generic class implementation. fixup noderefs for series winding of AutoTrans. Warning \*\*\*\* Magic happens here Redefine 2nd node of Series winding to same as first node of 2nd winding (common winding). |
| **Method-public** | GetCurrents | Get present current values of terminal. |
| **Property-public** | RotatePhases | For Delta connections or Line-Line voltages. |
| **Property-public** | PresentTap | PA Get\_PresentTap and Set\_PresentTap. |
| **Property-public** | Mintap | PA Get\_MinTap. |
| **Property-public** | Maxtap | PA Get\_MaxTap. |
| **Property-public** | TapIncrement | PA Get\_TapIncrement. |
| **Property-public** | BaseVoltage | PA Get\_BaseVoltage. |
| **Property-public** | BasekVLL | PA Get\_BasekVLL. |



***
_Created with the Standard Edition of HelpNDoc: [Transform Your CHM Help File Creation Process with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
