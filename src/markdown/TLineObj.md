# TLineObj

| ***TLineObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Method-private** | FMakeZFromGeometry | Make new Z, Zinv, Yc, etc. from line geometry reference. |
| **Method-private** | KillGeometrySpecified | Indicate No Line Geometry specification if this is called. |
| **Method-private** | FMakeZFromSpacing | make new Z, Zinv, Yc, etc. from linespacing reference. |
| **Method-private** | KillSpacingSpecified | Indicate No Line spacing specification if this is called. |
| **Method-private** | ClearYPrim | Clears the Y primitive memory spaces. |
| **Method-private** | ResetLengthUnits | Resets the length units to the default. |
| **Method-private** | UpdatePDProperties | Updates inherited properties. |
| **Property-private** | NumConductorData | Defines the number of conductors for the element. |
| **Property-private** | FetchConductorData | Gets the conductor data from the conductor data reference. |
| **Method-private** | ReallocZandYcMatrices | Reallocate Z and Y matrices in memory (possible expansion). |
| **Method-private** | DoLongLine | Long Line Correction for 1=phase. |
| **Method-private** | ConvertZinvToPosSeqR | For GIC analysis, primarily. Uses only real part of Z. |
| **Method-public** | GetLosses | Overrides the more specific class specification. Calculates the losses for the area. |
| **Method-public** | GetSeqLosses | Overrides the more specific class specification. Calculates the losses for the area using sequential components. |
| **Method-public** | RecalcElementData | See 3.1.9. |
| **Method-public** | CalcYPrim | See 3.1.9. |
| **Method-public** | MakePosSequence | See 3.1.9. |
| **Property-public** | MergeWith | Merge this line with another line and disable the other line. |
| **Method-public** | UpdateControlElements | Updates the elements controlled/assigned to the controllers in the model. |
| **Property-public** | GetPropertyValue | See 3.1.9. |
| **Method-public** | InitPropertyValues | See 3.1.9. |
| **Method-public** | DumpProperties | See 3.1.9. |
| **Method-public** | FetchLineCode | Loads the line code given in the argument into the active line. |
| **Method-public** | FetchGeometryCode | Loads the line geometry given in the argument into the active line. |
| **Method-public** | FetchLineSpacing | Loads the line spacing given in the argument into the active line. |
| **Method-public** | FetchWireList | Loads the wire data given in the argument into the active line. |
| **Method-public** | FetchCNCableList | Loads the CNCable data given in the argument into the active line. |
| **Method-public** | FetchTSCableList | Loads the TSCable data given in the argument into the active line. |
| **Method-public** | CalcFltRate | Overrides the generic class declaration. Calculates failure rates for section and buses. |



***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Productivity with HelpNDoc's Efficient User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
