# TLineGeometryObj

| ***TLineGeometryObj*** |  |  |  |  |
| --- | --- | --- | --- | --- |
| ***Type-access*** |  | *Command* | *Description* |  |
| **Implements the following properties/methods as in TLoadShapeObj and TLineObj:** **InitPropertyValues**&nbsp; **DumpProperties** **GetPropertyValue** **SaveWrite** |  |  |  |  |
| **Method-private** | ChangeLineConstantsType |  |  | Reallocates memory for hosting the given number of phases. |
| **Method-private** | set\_Nconds |  |  | Sets the number of conductors for this line geometry. |
| **Method-private** | set\_Nphases |  |  | Sets the number of phases for this line geometry. |
| **Method-private** | set\_ActiveCond |  |  | Sets the given conductor number to be the active conductor. |
| **Method-private** | Get\_YCmatrix |  |  | Returns the Y matrix for this element. |
| **Method-private** | Get\_Zmatrix |  |  | Returns the Z matrix for this element. |
| **Method-private** | Get\_RhoEarth |  |  | Gets the rho earth value for the line model. |
| **Method-private** | Set\_RhoEarth |  |  | Sets the rho earth value for the line model. |
| **Property-private** | get\_Nconds |  |  | Returns the number of conductors for this line model. |
| **Method-private** | UpdateLineGeometryData |  |  | Call this before using the line data. Implements the routine for importing the wire/cable data values linked to this model. |
| **Property-private** | Get\_FX |  |  | Gets X for the given index. |
| **Property-private** | Get\_FY |  |  | Gets Y for the given index. |
| **Property-private** | Get\_Funits |  |  | Returns the units for the active conductor. |
| **Property-private** | Get\_ConductorName |  |  | Returns the name for the active conductor. |
| **Property-private** | Get\_ConductorData |  |  | Returns the conductor data object for the active conductor. |
| **Property-private** | Get\_PhaseChoice |  |  | Returns the phase choice for the active conductor. |
| **Property-public** | Xcoord |  |  | PA Get\_FX. |
| **Property-public** | Ycoord |  |  | PA Get\_FY. |
| **Property-public** | Nwires |  |  | PA FNConds (variable) and set\_Nwires. |
| **Property-public** | Nphases |  |  | PA FNPhases (variable) and set\_Nphases. |
| **Property-public** | Units |  |  | PA Get\_FUnits . |
| **Method-public** | LoadSpacingAndWires |  |  | Called from a Line object that has its own Spacing and Wires input automatically sets reduce=y if the spacing has more wires than phases. |
| **Property-public** | Nconds |  |  | PA get\_Nconds and set\_Nconds. |
| **Property-public** | ActiveCond |  |  | PA FActiveCond (variable) and set\_ActiveCond. |
| **Property-public** | Zmatrix |  |  | PA Get\_Zmatrix. |
| **Property-public** | YCmatrix |  |  | PA Get\_YCmatrix. |
| **Property-public** | RhoEarth |  |  | PA Get\_RhoEarth and Set\_RhoEarth. |
| **Property-public** | ConductorName |  |  | PA Get\_ConductorName. |
| **Property-public** | ConductorData |  |  | PA Get\_ConductorData. |
| **Property-public** | NWires |  |  | PA FNConds (variable). |
| **Property-public** | PhaseChoice |  |  | PA Get\_PhaseChoice. |



***
_Created with the Standard Edition of HelpNDoc: [Free help authoring tool](<https://www.helpndoc.com/help-authoring-tool>)_
