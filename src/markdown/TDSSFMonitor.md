# TDSSFMonitor

| ***TDSSFMonitor*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Implements the following properties/methods as in TMeterClass and 3.1.4:** **DefineProperties** **MakeLike** **Edit** **Init** **NewObject** |  |  |
| **Method-public** | ResetAll | Reset all meters in active circuit to zero. Overrides the more generic class. |
| **Method-public** | SampleAll | Forces all meters in active circuit to sample. Overrides the more generic class. |
| **Method-public** | SaveAll | Forces all meters in the circuit to take a sample. Overrides the more generic class. |
| **Method-public** | update\_sys\_ld\_info | Updates the latest simulation data for all Fmonitors. |
| **Method-public** | Calc\_P\_freq | Calculates frequency for each cluster. |
| **Method-public** | update\_atks | Updates the attack variables for all Fmonitors. |
| **Method-public** | update\_defense\_layer | Updates the defense layer for all Fmonitors. |



***
_Created with the Standard Edition of HelpNDoc: [Transform Your Documentation Process with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
