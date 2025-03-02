# TTransf

| ***TTransf*** |  |  |  |
| --- | --- | --- | --- |
| ***Type-access*** |  | *Command* | *Description* |
| **Implements the following properties/methods as in TLine:** **DefineProperties** **MakeLike** **Edit** **Init** **NewObject** |  |  |  |
| **Method-private** | SetActiveWinding |  | Sets the active winding using the given integer. |
| **Method-private** | InterpretAutoConnection |  | Interprets the connection for the active winding. |
| **Method-private** | InterpretAllConns |  | Interprets the connection for all windings. |
| **Method-private** | InterpretAllBuses |  | Assigns buses to all windings. |
| **Method-private** | InterpretAllTaps |  | Assigns active tap position to all windings. |
| **Method-private** | InterpretAllkVRatings |  | Assigns kV ratings to all windings. |
| **Method-private** | InterpretAllkVARatings |  | Assigns kVA ratings to all windings. |
| **Method-private** | InterpretAllRs |  | Assigns Percent ac resistance to all windings. |
| **Property-private** | TrapZero |  | Trap for catching 0 to avoid numeric overflows during calculations. |
| **Property-private** | InterpretLeadLag |  | Routine expecting all winding bus connections expressed in one array of strings. |


&nbsp;

![A picture containing chart

Description automatically generated](<lib/NewItem605.png>)

**Figure 1. PDE object inheritance tree**

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Word Document into a Professional eBook with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
