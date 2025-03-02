# TLoadShapeObj

| ***TLoadShapeObj*** |  |  |  |  |
| --- | --- | --- | --- | --- |
| ***Type-access*** |  | *Command* | *Description* |  |
| **Implements the following properties/methods as in TConductorDataObj:** **InitPropertyValues**&nbsp; **DumpProperties** **GetPropertyValue** |  |  |  |  |
| **Property-private** | Get\_Interval |  |  | Returns the present time interval. |
| **Method-private** | Set\_NumPoints |  |  | Updates the number of points for the shape. |
| **Method-private** | SaveToDblFile |  |  | Saves the shape into a DBL file. |
| **Method-private** | SaveToSngFile |  |  | Saves the shape into a SNG file. |
| **Method-private** | CalcMeanandStdDev |  |  | Calculates the mean and standard deviation for the shape. |
| **Method-private** | Get\_Mean |  |  | Returns the latest mean calculated. |
| **Method-private** | Get\_StdDev |  |  | Returns the latest standard deviation calculated. |
| **Method-private** | Set\_Mean |  |  | Updates the mean using the given value. |
| **Method-private** | Set\_StdDev |  |  | Normalize the curve presently in memory. |
| **Method-private** | SetMaxPandQ |  |  | Obtains the maximum P and Q from the curves already loaded in memory. |
| **Property-public** | GetMult |  |  | Get multiplier at specified time. |
| **Property-public** | Mult |  |  | Get multiplier by index. |
| **Property-public** | Hour |  |  | Get hour corresponding to point index. |
| **Method-public** | Normalize |  |  | Normalizes the waveform in memory. |
| **Method-public** | LoadMMFView |  |  | Loads the current view of the MMF into memory for further use. |
| **Method-public** | LoadFileFeatures |  |  | Loads the mapped file features into local variables for further use. |
| **Property-public** | NumPoints |  |  | PA FNumPoints (variable) and Set\_NumPoints. |
| **Property-public** | PresentInterval |  |  | PA Get\_Interval. |
| **Property-public** | Mean |  |  | PA Get\_Mean and Set\_Mean. |
| **Property-public** | StdDev |  |  | PA Get\_StdDev and Set\_StdDev. |



***
_Created with the Standard Edition of HelpNDoc: [Qt Help documentation made easy](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
