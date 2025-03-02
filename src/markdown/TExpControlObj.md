# TExpControlObj

| ***TExpControlObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Implements the following properties/methods as in TCapControlObj:** **RecalcElementData** **CalcYPrim** **GetLosses** **GetPropertyValue** **InitPropertyValues** **DumpProperties** **SaveWrite** **MakePosSequence** **Sample** **DoPendingAction** **Reset** **Set\_PendingChange** **Get\_PendingChange** |  |  |
| **Property-private** | ReturnElementsList | Returns the list of elements controlled by this controller, the list is delivered as string. |
| **Method-private** | UpdateExpControl | Updates the state variables at the present simulation time/mode. |
| **Method-public** | GetInjCurrents | See 3.1.9. |
| **Method-public** | GetCurrents | See 3.1.9. |
| **Property-public** | MakePVSystemList | Allocates memory and creates the list of PV systems to be controlled. |
| **Property-public** | PendingChange | PA Get\_PendingChange and Set\_PendingChange. |
| **Property-public** | DERNameList | PA FDERNameList (variable). |
| **Property-public** | VregTau | PA FVregTau (variable). |
| **Property-public** | QVSlope | PA FSlope (variable). |
| **Property-public** | VregMin | PA FVregMin (variable). |
| **Property-public** | VregMax | PA FVregMax (variable). |
| **Property-public** | QMaxLead | PA FQMaxLead (variable). |
| **Property-public** | QMaxLag | PA FQMaxLag (variable). |
| **Property-public** | TResponse | PA FTResponse (variable). |



***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Output with HelpNDoc's Stunning User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
